var coll = document.getElementsByClassName("chapter-title");

var lastExpanded = null;

for (var i = 0; i < coll.length; i++) {
    if (coll[i].classList.contains("ignore")) {
        continue;
    }
    coll[i].addEventListener("click", function() {
        // Expand/collapse the clicked one
        this.classList.toggle("chapter-title-active");
        var content = this.nextElementSibling;
        // If there is something already expanded, collapse it
        if (lastExpanded != null && lastExpanded != this) {
            lastExpanded.nextElementSibling.style.maxHeight = null;
            lastExpanded.nextElementSibling.style.border = null;
            lastExpanded.classList.toggle("chapter-title-active");
        }
        lastExpanded = null;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
            content.style.border = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
            content.style.border = "1px solid var(--main-text)";
            lastExpanded = this;
        }
    });
}

// Copy code functionality for pseudo-code blocks
document.addEventListener('DOMContentLoaded', function() {
    var copyButtons = document.querySelectorAll('.copy-code-btn');

    copyButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();

            var codeBlock = this.parentElement;
            var rawCode = codeBlock.getAttribute('data-code');

            // Clean up the code (remove extra whitespace from first line, etc)
            var lines = rawCode.split('\n');
            // Remove first empty line if exists
            if (lines.length > 0 && lines[0].trim() === '') {
                lines.shift();
            }
            var cleanCode = lines.join('\n');

            // Copy to clipboard
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(cleanCode).then(function() {
                    showCopySuccess(button);
                }).catch(function(err) {
                    console.error('Failed to copy:', err);
                    fallbackCopy(cleanCode, button);
                });
            } else {
                fallbackCopy(cleanCode, button);
            }
        });
    });

    function showCopySuccess(button) {
        var copyIcon = button.querySelector('.copy-icon');
        var checkIcon = button.querySelector('.check-icon');

        // Hide copy icon, show check icon
        copyIcon.style.display = 'none';
        checkIcon.style.display = 'inline';
        button.classList.add('copied');

        // Reset after 2 seconds
        setTimeout(function() {
            copyIcon.style.display = 'inline';
            checkIcon.style.display = 'none';
            button.classList.remove('copied');
        }, 2000);
    }

    function fallbackCopy(text, button) {
        var textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        document.body.appendChild(textArea);
        textArea.select();

        try {
            var successful = document.execCommand('copy');
            if (successful) {
                showCopySuccess(button);
            }
        } catch (err) {
            console.error('Fallback copy failed:', err);
        }

        document.body.removeChild(textArea);
    }
});

// Dark mode theme switching
(function() {
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;

    // Check for saved theme preference or default to system preference
    const getPreferredTheme = () => {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            return savedTheme;
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    };

    // Apply theme
    const setTheme = (theme) => {
        html.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    };

    // Initialize theme on page load
    setTheme(getPreferredTheme());

    // Toggle theme on button click
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
        });
    }

    // Listen for system preference changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });
})();