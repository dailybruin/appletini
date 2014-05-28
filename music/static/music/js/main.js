var color_thief = new ColorThief();

var recolorBackground = function($album_cover) {
    var rgb = color_thief.getColor($album_cover),
        color_string = 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')';

    $($album_cover).parents('.album').css('background-color', color_string);
};

$('.albums').imagesLoaded(function() {
    Array.prototype.forEach.call($('.album-artwork'), function($a) {
        recolorBackground($a);
    });
});

// AJAX review loading:
$('.album').click(function() {
    var $this = $(this),
        $review_loaded = $this.attr('data-review-loaded');

    if ($review_loaded === 'false') {
        $.ajax({
            type: 'POST',
            url: $this.attr('data-review-url') + '?json=1',
            success: function(data) {
                // TODO: place data into .review-album child
                console.log(data);

                toggleAlbumReview($this);
            }
        });

        return;
    }

    toggleAlbumReview($this);
});

function toggleAlbumReview($album) {
    $album.children('.album-review').toggle();
}

