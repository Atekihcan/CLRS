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