$(function () {
    $('textarea[data-editor]').each(function () {
        var textarea = $(this);
        var mode = textarea.data('editor');
        var editDiv = $('<div>', {
            position: 'absolute',
            width: textarea.width(),
            height: textarea.height(),
            'class': textarea.attr('class')
        }).insertBefore(textarea);

        textarea.css('visibility', 'hidden');
        var editor = ace.edit(editDiv[0]);
        var original = textarea.val();
        editor.renderer.setShowGutter(true);
        editor.getSession().setValue(original);
        editor.getSession().setMode("ace/mode/" + mode);
        editor.setTheme("ace/theme/xcode");
        
        // copy back to textarea on form submit...
        editor.getSession().on('change', function () {
            textarea.val(editor.getSession().getValue());
        })
        
        $('#clrs-reset').on("click", function() {
            editor.getSession().setValue(original);
        })
    });
});