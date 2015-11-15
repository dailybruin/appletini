// Inital location for map
var position = [34.0708189, -118.4531212];
// URL for spreadsheet with data
var dataURL = "https://spreadsheets.google.com/feeds/list/1eIxoc4h6B2nTdDAitHkviJH5rtH-MNyBaEUS7zHmKk0/od6/public/values?alt=json";
// Pin images for map
var normalPinURL = "http://dailybruin.com/images/2015/05/pin.png";
var highlightedPinURL = "http://dailybruin.com/images/2015/05/highlighted-pin.png";
var map; 

function showGoogleMaps() {

    var latLng = new google.maps.LatLng(position[0], position[1]);

    gc = new google.maps.Geocoder;
    gc.geocode( { 'address' : 'University of California, Los Angeles, CA' }, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      center = new google.maps.LatLng(results[0].geometry.location.lat(), results[0].geometry.location.lng());

    var mapOptions = {
      zoom: 11, // initialize zoom level - the max value is 21
      streetViewControl: false, // hide the yellow Street View pegman
      scaleControl: false, // allow users to zoom the Google Map
      panControl: false,
      navigationControl: false,
      mapTypeControl: false,
      scrollwheel: false,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      center: latLng,
      zoomControlOptions: {
        style: google.maps.ZoomControlStyle.LARGE,
        position: google.maps.ControlPosition.RIGHT_CENTER
      },
    };

    map = new google.maps.Map(document.getElementById('googlemaps'),
        mapOptions);

    addDataToMap();
    }
});
}

google.maps.event.addDomListener(window, 'load', showGoogleMaps);