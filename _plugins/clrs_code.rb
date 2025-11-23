# frozen_string_literal: true

# CLRSCode: Jekyll plugin for rendering CLRS-style pseudocode
# Converts plain text pseudocode to KaTeX-compatible LaTeX
#
# Usage in markdown:
#   {% capture code %}
#   for i = 1 to n
#       A[i] = A[Parent(i)]
#   {% endcapture %}
#   {% include clrs_code.html title="Procedure-Name(A, n)" %}

module CLRSCode
  # Extensible configuration for keywords
  CONFIG = {
    # Bold keywords (control flow) - rendered with \textbf
    conditionals: %w[
      if elseif else for while to downto
      return error continue break and or not
    ],

    # Regular weight keywords - rendered with \text
    # Note: single letters like 'a' removed to avoid matching variables
    keywords: %w[
      swap exchange with let be an new array arrays
      matrix matrices partition sort using as keys is empty
      total number of size across all each same than fewer
      contained length first from minimum list lists
      min-heap max-heap true false
    ],

    # Constants - rendered with \textsc
    constants: %w[TRUE FALSE NIL],

    # Floor/ceiling delimiters
    delimiters: %w[floor ceil],

    # Symbol replacements (order matters for multi-char sequences)
    symbols: {
      '...'  => '\dots',
      '<='   => '\leq',
      '>='   => '\geq',
      '!='   => '\ne',
      '=='   => '=',
      '*'    => '\cdot',
      ' % '  => ' \\bmod ',
      'infinity' => '\infty',
      'INFINITY' => '\infty'
    },

    # Unicode symbol replacements
    # Note: ceiling/floor add spacing to separate from adjacent content
    unicode_symbols: {
      "\u00D7" => '\\times',    # ×
      "\u221E" => '\infty',     # ∞
      "\u2260" => '\ne',        # ≠
      "\u2264" => '\leq',       # ≤
      "\u2265" => '\geq',       # ≥
      "\u2308" => '\lceil ',    # ⌈ (space after)
      "\u2309" => ' \rceil',    # ⌉ (space before)
      "\u230A" => '\lfloor ',   # ⌊ (space after)
      "\u230B" => ' \rfloor'    # ⌋ (space before)
    }
  }.freeze

  # Tokenizer: Splits a line into meaningful tokens
  # Handles nested brackets, parentheses, and quoted strings
  class Tokenizer
    def initialize(line)
      @line = line
      @pos = 0
      @tokens = []
    end

    def tokenize
      @tokens = []
      @pos = 0

      while @pos < @line.length
        char = @line[@pos]

        case char
        when ' ', "\t"
          # Skip whitespace but mark token boundaries
          @pos += 1
        when '"'
          # Quoted string
          @tokens << read_quoted_string
        when '/'
          # Check for comment
          if @line[@pos + 1] == '/'
            @tokens << read_comment
          else
            @tokens << read_token
          end
        else
          @tokens << read_token unless char.strip.empty?
        end
      end

      @tokens.compact.reject(&:empty?)
    end

    private

    def read_token
      start = @pos
      depth_bracket = 0
      depth_paren = 0

      while @pos < @line.length
        char = @line[@pos]

        case char
        when '['
          depth_bracket += 1
          @pos += 1
        when ']'
          depth_bracket -= 1
          @pos += 1
          # Only break if we've closed all brackets
          break if depth_bracket <= 0 && depth_paren <= 0
        when '('
          depth_paren += 1
          @pos += 1
        when ')'
          depth_paren -= 1
          @pos += 1
          # Only break if we've closed all parens and not inside bracket
          break if depth_paren <= 0 && depth_bracket <= 0
        when ' ', "\t"
          # Space breaks token unless inside brackets/parens
          break if depth_bracket <= 0 && depth_paren <= 0
          @pos += 1
        when '"'
          # Don't consume quote as part of token
          break
        else
          @pos += 1
        end
      end

      @line[start...@pos].strip
    end

    def read_quoted_string
      @pos += 1  # Skip opening quote
      start = @pos

      while @pos < @line.length && @line[@pos] != '"'
        @pos += 1
      end

      content = @line[start...@pos]
      @pos += 1 if @pos < @line.length  # Skip closing quote

      { type: :string, content: content }
    end

    def read_comment
      start = @pos
      @pos = @line.length  # Comment extends to end of line
      { type: :comment, content: @line[start..] }
    end
  end

  # Formatter: Converts tokens to LaTeX
  class Formatter
    def initialize
      @delimiter_stack = []
    end

    def format_line(line, line_number, offset = 0)
      # Calculate indentation
      indentation = calculate_indentation(line)
      tabs = '\quad ' + ('\qquad ' * indentation)

      # Apply symbol replacements first
      processed_line = apply_symbol_replacements(line)

      # Tokenize
      tokenizer = Tokenizer.new(processed_line.strip)
      tokens = tokenizer.tokenize

      # Format tokens
      latex_parts = []
      is_comment = false

      tokens.each_with_index do |token, idx|
        if token.is_a?(Hash)
          case token[:type]
          when :comment
            latex_parts << format_comment(token[:content], idx == 0)
            is_comment = true
          when :string
            latex_parts << format_string(token[:content])
          end
        elsif is_comment
          latex_parts << format_comment_word(token)
        else
          latex_parts << format_token(token, idx == 0)
        end
      end

      latex = latex_parts.join('')
      actual_offset = offset.to_i
      display_line_num = line_number + actual_offset

      "#{display_line_num}& #{tabs} #{latex} \\\\"
    end

    private

    def calculate_indentation(line)
      spaces = line.match(/^(\s*)/)&.[](1)&.length || 0
      spaces / 4
    end

    def apply_symbol_replacements(line)
      # Split line at comment if present, only apply replacements to code part
      if line.include?('//')
        comment_idx = line.index('//')
        code_part = line[0...comment_idx]
        comment_part = line[comment_idx..]
      else
        code_part = line
        comment_part = ''
      end

      result = code_part.dup

      # Apply unicode replacements first
      CLRSCode::CONFIG[:unicode_symbols].each do |symbol, replacement|
        result = result.gsub(symbol, replacement)
      end

      # Apply multi-char replacements (order matters)
      CLRSCode::CONFIG[:symbols].each do |symbol, replacement|
        result = result.gsub(symbol, replacement)
      end

      # Add spacing after commas (but preserve structure) - only in code part
      result = result.gsub(/,(?!\s*\\,)/, ', \,')

      result + comment_part
    end

    def format_token(token, is_first)
      spacing = is_first ? '' : '\,'

      # Check for different token types based on structure
      # Priority order matters: function calls before brackets (functions may have array args)
      if delimiter_function?(token)
        "#{spacing}#{format_delimiter_function(token)}"
      elsif function_call?(token)
        "#{spacing}#{format_function_call(token)}"
      elsif contains_brackets?(token)
        "#{spacing}#{format_bracketed(token)}"
      elsif contains_parens?(token)
        "#{spacing}#{format_with_parens(token)}"
      elsif keyword?(token)
        format_keyword(token, is_first)
      elsif conditional?(token)
        format_conditional(token, is_first)
      elsif constant?(token)
        "#{spacing}\\textsc{#{token}}"
      elsif subscript?(token)
        format_subscript(token, spacing)
      elsif hyphenated_variable?(token)
        "#{spacing}#{format_hyphenated_variable(token)}"
      else
        "#{spacing}#{token}"
      end
    end

    def delimiter_function?(token)
      token.match?(/^(floor|ceil)\(/)
    end

    def function_call?(token)
      # Match function call pattern: Name(args) or Name`(args)
      # Function names can contain hyphens like Binary-Search
      token.match?(/^[A-Za-z][A-Za-z0-9-]*`?\(.*\)$/)
    end

    def contains_brackets?(token)
      token.include?('[')
    end

    def contains_parens?(token)
      token.include?('(')
    end

    def keyword?(token)
      CLRSCode::CONFIG[:keywords].include?(token.downcase)
    end

    def conditional?(token)
      CLRSCode::CONFIG[:conditionals].include?(token.downcase)
    end

    def constant?(token)
      CLRSCode::CONFIG[:constants].include?(token)
    end

    def subscript?(token)
      token.include?('_') && !token.include?('[') && !token.include?('(')
    end

    def hyphenated_variable?(token)
      # Match variable names with hyphens like min-index, heap-size
      # Also match patterns with dots like A.heap-size or Array-Original.heap-size
      # Must contain at least one hyphen, no parentheses or brackets
      return false if token.include?('(') || token.include?('[')
      return false unless token.include?('-')
      # Must be valid identifier parts separated by hyphens and/or dots
      token.match?(/^[a-zA-Z][a-zA-Z0-9]*([.\-][a-zA-Z][a-zA-Z0-9]*)*$/)
    end

    def format_hyphenated_variable(token)
      # Render hyphenated variables in italic with literal hyphen
      # Split by hyphen, wrap each part, join with \text{-}
      parts = token.split('-')
      parts.join('\\text{-}')
    end

    # Format array access: A[...] where content inside can be variable or function
    def format_bracketed(token)
      # Find the array name (may include hyphens or dots) and bracket content
      match = token.match(/^([A-Za-z][A-Za-z0-9\-.]*)(\[.+\])(.*)$/)
      return token unless match

      array_name = match[1]
      bracket_expr = match[2]
      suffix = match[3] || ''

      # Format array name (may be hyphenated)
      formatted_name = if hyphenated_variable?(array_name)
                         format_hyphenated_variable(array_name)
                       else
                         array_name
                       end

      # Parse bracket content recursively
      inner_content = bracket_expr[1...-1]  # Remove [ and ]
      formatted_inner = format_bracket_content(inner_content)

      "#{formatted_name}[#{formatted_inner}]#{suffix}"
    end

    def format_bracket_content(content)
      # Content inside brackets can be:
      # - Simple variable: i, j, k
      # - Function call: Parent(i), Random(1, n)
      # - Multi-dimensional: i, j (with commas)
      # - Expression: i + 1, j - 1

      parts = split_bracket_content(content)
      formatted_parts = parts.map { |part| format_bracket_part(part.strip) }
      formatted_parts.join(', \,')
    end

    def split_bracket_content(content)
      # Split by comma but respect nested parens
      parts = []
      current = ''
      depth = 0

      content.each_char do |char|
        case char
        when '('
          depth += 1
          current += char
        when ')'
          depth -= 1
          current += char
        when ','
          if depth == 0
            parts << current
            current = ''
          else
            current += char
          end
        else
          current += char
        end
      end

      parts << current unless current.empty?
      parts
    end

    def format_bracket_part(part)
      # Check if this part is a function call
      if part.match?(/^[A-Za-z][A-Za-z0-9-]*`?\(/)
        format_function_call(part)
      elsif hyphenated_variable?(part)
        format_hyphenated_variable(part)
      else
        part
      end
    end

    # Format function/procedure calls: Name(args) or Name`(args)
    def format_with_parens(token)
      # Check for delimiter functions (floor, ceil)
      if token.match?(/^(floor|ceil)\(/)
        return format_delimiter_function(token)
      end

      # Check for function call pattern: Name(args) or Name`(args) - including empty parens
      match = token.match(/^([A-Za-z][A-Za-z0-9-]*?)(`?)(\(.*\))$/)
      if match
        format_function_call(token)
      else
        # Just parentheses, not a function call (e.g., grouped expression)
        token
      end
    end

    def format_function_call(token)
      # Match function name (possibly with prime) and arguments
      match = token.match(/^([A-Za-z][A-Za-z0-9-]*?)(`?)(\(.*\))$/)
      return token unless match

      func_name = match[1]
      prime = match[2]
      args_with_parens = match[3]

      # Extract arguments (remove outer parens)
      args_content = args_with_parens[1...-1]

      # Process arguments recursively
      formatted_args = format_function_args(args_content)

      # Format: \textsc{FuncName}'(args)
      prime_latex = prime == '`' ? "'" : ''
      "\\textsc{#{func_name}}#{prime_latex}(#{formatted_args})"
    end

    def format_function_args(content)
      return '' if content.nil? || content.strip.empty?

      # Split by comma respecting nested parens/brackets
      parts = split_function_args(content)
      formatted_parts = parts.map { |part| format_function_arg(part.strip) }
      formatted_parts.join(', ')
    end

    def split_function_args(content)
      parts = []
      current = ''
      depth_paren = 0
      depth_bracket = 0

      content.each_char do |char|
        case char
        when '('
          depth_paren += 1
          current += char
        when ')'
          depth_paren -= 1
          current += char
        when '['
          depth_bracket += 1
          current += char
        when ']'
          depth_bracket -= 1
          current += char
        when ','
          if depth_paren == 0 && depth_bracket == 0
            parts << current
            current = ''
          else
            current += char
          end
        else
          current += char
        end
      end

      parts << current unless current.empty?
      parts
    end

    def format_function_arg(arg)
      # Process each argument - could be a variable, array access, function call, or subscript
      if function_call?(arg)
        format_function_call(arg)
      elsif arg.include?('[')
        format_bracketed(arg)
      elsif hyphenated_variable?(arg)
        format_hyphenated_variable(arg)
      elsif subscript?(arg)
        format_subscript_simple(arg)
      else
        arg
      end
    end

    def format_subscript_simple(token)
      # Format subscript: A_11 -> A_{11}
      parts = token.split('_', 2)
      "#{parts[0]}_{#{parts[1]}}"
    end

    def format_delimiter_function(token)
      # Match floor/ceil with optional whitespace inside parens
      match = token.match(/^(floor|ceil)\(\s*(.+?)\s*\)$/)
      return token unless match

      delim_type = match[1]
      content = match[2].strip

      case delim_type
      when 'floor'
        "\\lfloor #{content} \\rfloor"
      when 'ceil'
        "\\lceil #{content} \\rceil"
      end
    end

    def format_keyword(token, is_first)
      if is_first
        "\\text{#{token}}"
      else
        "\\,\\text{#{token}}"
      end
    end

    def format_conditional(token, is_first)
      if is_first
        "\\textbf{#{token} }"
      else
        "\\textbf{ #{token} }"
      end
    end

    def format_subscript(token, spacing)
      parts = token.split('_', 2)
      "#{spacing}#{parts[0]}_{#{parts[1]}}"
    end

    def format_comment(content, is_first)
      prefix = is_first ? '' : '\quad '
      # content includes the // prefix, extract the text after it
      comment_text = content.sub(/^\/\/\s*/, '')

      # Format each word in the comment
      formatted_words = comment_text.split(/\s+/).map do |word|
        format_comment_word(word)
      end.join('')

      "#{prefix}\\textbf{/\\!/} #{formatted_words}"
    end

    def format_comment_word(token)
      return '' if token.nil? || token.empty?
      # Check if it's a symbol/number or a word
      if token.match?(/^[0-9+\-*\/\[\]\(\)\{\}\.\,]+$/)
        token
      else
        "\\text{ #{token}}\\,"
      end
    end

    def format_string(content)
      "\\text{\\textquotedblleft #{content}\\textquotedblright} "
    end
  end

  # Format procedure title: Build-Max-Heap`(A) -> \textsc{Build-Max-Heap}'(A)
  def self.format_title(title)
    return '' if title.nil? || title.empty?

    # Check if has parentheses (may be empty or with parameters)
    if title.include?('(')
      match = title.match(/^([A-Za-z][A-Za-z0-9-]*?)(`?)(\(.*\))$/)
      if match
        func_name = match[1]
        prime = match[2]
        params = match[3]
        prime_latex = prime == '`' ? "'" : ''
        "$$\\textsc{#{func_name}}#{prime_latex}#{params}$$"
      else
        "$$#{title}$$"
      end
    else
      # No parameters, just procedure name
      match = title.match(/^([A-Za-z][A-Za-z0-9-]*)(`?)$/)
      if match
        func_name = match[1]
        prime = match[2]
        prime_latex = prime == '`' ? "'" : ''
        "$$\\textsc{#{func_name}}#{prime_latex}$$"
      else
        "$$#{title}$$"
      end
    end
  end

  # Main entry point: format entire code block
  def self.format_code(code, offset = nil)
    actual_offset = offset.to_i  # Handle nil, string, or integer
    formatter = Formatter.new
    lines = code.to_s.split("\n")

    # Skip first empty line if present
    start_idx = lines.first&.strip&.empty? ? 1 : 0

    formatted_lines = []
    line_num = 1

    lines[start_idx..].each do |line|
      next if line.strip.empty? && formatted_lines.empty?  # Skip leading empty lines

      formatted_lines << formatter.format_line(line, line_num, actual_offset)
      line_num += 1
    end

    formatted_lines.join("\n")
  end
end

# Make module available to Liquid templates
module Jekyll
  module CLRSCodeFilter
    def clrs_format_title(title)
      CLRSCode.format_title(title)
    end

    def clrs_format_code(code, offset = 0)
      CLRSCode.format_code(code, offset)
    end
  end
end

Liquid::Template.register_filter(Jekyll::CLRSCodeFilter)
