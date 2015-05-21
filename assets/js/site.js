$(document).ready(function() {
    $(".show-hide-button").click(function(){
        $(this).next(".show-hide").slideToggle("fast");
        var text_label = $(".show-hide-button", this).text();
        var text_len   = text_label.length;
        ($(".show-hide-button", this).text().slice(0, 1) == "\u25B6") ? $(".show-hide-button", this).text("\u25BC " + text_label.slice(1, text_len)) : $(".show-hide-button", this).text("\u25B6 " + text_label.slice(1, text_len));
    });

    // Capitalize first letter of each word
    capitalizeFirst('.cflew');

    // Initialize the plugin
    $('#popupBox').popup({
        transition: 'all 0.3s'
    });
});

function capitalizeFirst(elem) {
    var words = $(elem).text().split(' ');
    var html = '';
    $.each(words, function() {
        html += this.substring(0,1)+'<span style="font-size:80%">'+this.substring(1)+'</span> ';
    });
    $(elem).html(html);
}