var map;
var center; 
var url = "https://spreadsheets.google.com/feeds/list/1eIxoc4h6B2nTdDAitHkviJH5rtH-MNyBaEUS7zHmKk0/od6/public/values?alt=json";
var data = []; 
var gc;
var markers = new Array();
var normalPinURL = "http://dailybruin.com/images/2015/05/pin.png";
var highlightedPinURL = "http://dailybruin.com/images/2015/05/highlighted-pin.png";
var currentIndex = 9; 
var highlightedPin = null;

function initialize() {
  gc = new google.maps.Geocoder;
  gc.geocode( { 'address' : 'University of California, Los Angeles, CA' }, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      center = new google.maps.LatLng(results[0].geometry.location.lat(), results[0].geometry.location.lng());

      map = new google.maps.Map(document.getElementById('content-map'), {
        streetViewControl: false, // hide the yellow Street View pegman
        scaleControl: false, // allow users to zoom the Google Map
        panControl: false,
        navigationControl: false,
        mapTypeControl: false,
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        center: center,
        zoom: 9
      });

      addDataToMap(); 
    }
  })

  setTimeout(function() {
    clickMarker(currentIndex);
  }, 3000)

}

var markers = new Array();
var currentCard = -1;
var autoMapScroll = 0;
var mapMarkers = new Array();
var infoWindows = new Array();
var pinToChange = null;
var currentPinIndex = -1;

// Gets data from Google Spreadsheets
function addDataToMap(){
  $.getJSON(dataURL, function(json){

    var data = {places: json.feed.entry};
    var content = document.getElementById("content")

    var source = $("#card_template").html(); 
    var template = Handlebars.compile(source)
    content.innerHTML = template(data);

    $.each(data.places, function (index, value){
      var loc; 

      var address = data.places[index]["gsx$place"]["$t"] + ", Los Angeles, CA";
      gc.geocode( { 'address' : address }, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
          loc = new google.maps.LatLng(results[0].geometry.location.lat(), results[0].geometry.location.lng());
        }

        var newURL = normalPinURL; 

        markers[markers.length] = new google.maps.Marker({
          position: loc,
          map: map,
          draggable: false,
          animation: google.maps.Animation.DROP,
          icon: newURL
        });

        var markerIndex = markers.length-1;
        google.maps.event.addListener(markers[markerIndex], 'click', function() {
          clickMarker(markerIndex);
        });



      // $("#content").append(cardTemp({apidata: data}));


      var cardID = '#card-' + index;

      $(window).bind('scroll', function() {
        if(currentCard > index || autoMapScroll != 0)
          return;

        if($(window).scrollTop() < 10)
        {
          panMapTo(0);
        }

        var position = $(cardID).offset().top + $(cardID).outerHeight() - window.innerHeight;
        if(currentCard == index && $(window).scrollTop() < position)
        {
          currentCard--;
          panMapTo(markerIndex-1);
        }

        if($(window).scrollTop() >= position && currentCard != index) {
          currentCard = index;
          panMapTo(markerIndex);
        }
      });
    });
});


    // Pan to first item at start
    panMapTo(0, true);
    currentPinIndex = -1;
  });
}

function clickMarker(markerIndex)
{
  if(markerIndex < 0)
  {
    autoMapScroll++;
    $('html, body').animate({
      scrollTop: 0
    }, 500);
    setTimeout(function (){
      autoMapScroll--;
    }, 530);

    currentPinIndex = -1;
    return;
  }
  if(!mapMarkers[markerIndex])
    return;
  if(autoMapScroll != 0)
  {
    $('html, body').clearQueue();
  }
  autoMapScroll++;
  $('html, body').animate({
    scrollTop: $("#card-" + (markerIndex)).offset().top-75
  }, 500);
  setTimeout(function (){
    autoMapScroll--;
  }, 530);

  panMapTo(markerIndex);
}

function panMapTo(markerIndex)
{
  panMapTo(markerIndex, false);
}

function panMapTo(markerIndex, override)
{ 
  if(!override && (markerIndex == 0 && currentPinIndex == -1))
  {
    currentPinIndex = 0;
    return;
  }
  if(!override &&(markerIndex == currentPinIndex))
    return;
  mapMarker = mapMarkers[markerIndex];
  if(!mapMarker)
    return;
  currentPinIndex = markerIndex;
  if(pinToChange)
    pinToChange.setIcon(normalPinURL);
  console.log('yes');
  mapMarker.setIcon(highlightedPinURL);
  pinToChange = mapMarker;
  map.panTo(mapMarker.position);
  if(!( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) )) {
    var offset = $(".card").width()/2;
    map.panBy(-offset-16, -30);
  }
}

function panToIndex(i) {
  m = markers[i];
  if(!m)
    return;
  currentIndex = i;
  if(highlightedPin)
    highlightedPin.setIcon(normalPinURL);
  m.setIcon(highlightedPinURL);
  highlightedPin = m;
  map.panTo(m.position);
}

function format(data){
  var result = [];
  var elem = {};
  var real_keyname = '';
  $.each(data.feed.entry, function(i, entry) {
    elem = {};
    $.each(entry, function(key, value){

      // fields that were in the spreadsheet start with gsx$
      if (key.indexOf("gsx$") == 0)
      {
        // get everything after gsx$
        formattedKey = key.substring(4);
        elem[formattedKey] = value['$t'];
      }
    });
    result.push(elem);
  });
  return result;
}
