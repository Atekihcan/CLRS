/*
 * Contains the site specific js
 */

$(document).ready(function() {
    $(".show-hide-button").click(function(){
        $(".show-hide").slideToggle("fast");
        ($(".show-hide-button").text() == "\u25B6 Show Calculation") ? $(".show-hide-button").text("\u25BC Hide Calculation") : $(".show-hide-button").text("\u25B6 Show Calculation");
    });
});