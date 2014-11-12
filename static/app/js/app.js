//JQuery extension for highlight
//(copied from my other project)
jQuery.fn.highlight = function () {
    $(this).each(function () {
        var el = $(this);
        $("<div/>")
            .width(el.outerWidth())
            .height(el.outerHeight())
            .css({
                "position": "absolute",
                "left": el.offset().left,
                "top": el.offset().top,
                "background-color": "#ffff99",
                "opacity": ".7",
                "z-index": "9999999"
            }).appendTo('body').fadeOut(5000).queue(function () { $(this).remove(); });
    });
}

