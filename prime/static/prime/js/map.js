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
var starURL = "";

console.log('hello');
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

      populateMap(); 
    }
  })

  setTimeout(function() {
    clickMarker(currentIndex);
  }, 3000)

}

var previous = function() {
  if (currentIndex == 0) {
    return;
  }

  currentIndex--;
  clickMarker(currentIndex);
  
  if (currentIndex == 0) {
    return;
  }
}

var next = function() {
  if (currentIndex == 11) {
    return;
  }

  currentIndex++;
  clickMarker(currentIndex);

  if (currentIndex == 11) {
    return;
  }
}

var populateMap = function() {
  $.getJSON(url, function(json){
    data = format(json); 

    var bubbles = []; 

    $.each(data, function (index, value){
      var loc; 

      var bubble = document.createElement("BUTTON");        
      var t = document.createTextNode(index + 1);    

      if (index == 9) {
        bubble.className = "content-bubble double-digit"
      }
      else {
        bubble.className = "content-bubble";
      }
      bubble.id = index; 

      if (index == 7 || index == 10 || index == 11) {
        bubble.innerHTML = '&#x2605;'
        bubble.className = "content-bubble star"
      }
      else {
        bubble.appendChild(t);
      }
      
      $(bubble).click(function() {
        console.log('this');
        clickMarker(bubble.id);
      })

      $('#content-nav').append(bubble);

      gc.geocode( { 'address' : data[index].address }, function(results, status) {
        // if (status == google.maps.GeocoderStatus.OK) {
          loc = new google.maps.LatLng(results[0].geometry.location.lat(), results[0].geometry.location.lng());
        // }

        var newURL;
        // if (index == 7 || index == 10 || index == 11) {
        //   newURL = starURL;
        // }
        // else {
          newURL = normalPinURL;
        // }

        markers[markers.length] = new google.maps.Marker({
          position: loc,
          map: map,
          draggable: false,
          // title: "0",
          animation: google.maps.Animation.DROP,
          icon: newURL
        });

        var markerIndex = markers.length-1;
        google.maps.event.addListener(markers[markerIndex], 'click', function() {
          clickMarker(markerIndex);
        });
      });
    });
  }); 
}

function clickMarker(i) {
  console.log(i);
  // refresh the box
  panToIndex(i);
  $('#content-place').html(data[i].cafe);
  var a = data[i].address.split(',');
  $('#content-address').html(data[i].address);
  var ind = '#' + i; 
  $('.active').removeClass('active');
  $(ind).addClass('active');
  var j = parseInt(i) + 1;
  $('#content-drink').html(data[i].drink);

  var src = 'img/' + j + '.jpg'
  $('#content-image img').attr('src', src)
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
