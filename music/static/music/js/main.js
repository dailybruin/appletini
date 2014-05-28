var colorThief = new ColorThief();

var recolorBackground = function($album_cover) {
    var rgb = colorThief.getColor($album_cover),
        color_string = 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')';

    $($album_cover).parent().css('background-color', color_string);
};

$('.albums').imagesLoaded(function() {
    Array.prototype.forEach.call($('.album-artwork'), function($a) {
        recolorBackground($a);
    });
});

$('.media.album').click(function() {

//AJAX request for spotify and wordpress URL's
var spotifyURL;
var wordpressURL;

//AJAX request for review text

var reviewText;

//Frontend visual changes to display review text and spotify playlist

});
