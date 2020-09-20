function capitalizeFirst(elem, method, sep) {
    var words = $(elem).text().split(sep);
    var html = '';
    $.each(words, function(i, val) {
        if (method && i < words.length - 1) {
            html += this.substring(0, 1) + '<span style="font-size:80%">' + this.substring(1) + '</span>-';
        } else {
            html += this.substring(0, 1) + '<span style="font-size:80%">' + this.substring(1) + '</span> ';
        }
    });
    $(elem).html(html);
}