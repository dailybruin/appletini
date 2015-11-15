// Here be dragons. Thou art forewarned.
// This file makes everything work
// To change basic settings, modify maps.js

// takes in JSON object from google sheets and turns into a json formatted
// this way based on the original google Doc
// [
//  {
//    'column1': info1,
//    'column2': info2,
//  }
// ]
function clean_google_sheet_json(data){
  var formatted_json = [];
  var elem = {};
  var real_keyname = '';
  $.each(data.feed.entry.reverse(), function(i, entry) {
    elem = {};
    $.each(entry, function(key, value){
      // fields that were in the spreadsheet start with gsx$
      if (key.indexOf("gsx$") == 0)
      {
        // get everything after gsx$
        real_keyname = key.substring(4);
        elem[real_keyname] = value['$t'];
      }
    });
    formatted_json.push(elem);
  });
  return formatted_json;
}

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
    console.log(data); 
    // console.log(data.places[0]["gsx$address"]);
    var content = getElementById('content');
    
    var source = $("#card-template").html(); 
    var template = Handlebars.compile(source)
    content.innerHTML = template(data);

    // $("#content").append(cardTemp({apidata: data}));
    $.each(data, function (index, value){
      mapMarkers[mapMarkers.length] = new google.maps.Marker({
        position: new google.maps.LatLng(value["lattitude"], value["longitude"]),
        map: map,
        draggable: false,
        animation: google.maps.Animation.DROP,
        title: value["title"],
        icon: normalPinURL
      });

      var markerIndex = mapMarkers.length-1;
      google.maps.event.addListener(mapMarkers[markerIndex], 'click', function() {
        clickPin(markerIndex);
      });

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
    })

    // Pan to first item at start
    panMapTo(0, true);
    currentPinIndex = -1;
  });
}

function clickPin(markerIndex)
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
  mapMarker.setIcon(highlightedPinURL);
  pinToChange = mapMarker;
  map.panTo(mapMarker.position);
  if(!( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) )) {
    var offset = $(".card").width()/2;
    map.panBy(-offset-16, -30);
  }
}