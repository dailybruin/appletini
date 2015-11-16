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
      console.log(data);
      // console.log(data.places[0]["gsx$address"]);
      var content = document.getElementById("content")
      
      var source = $("#card_template").html(); 
      var template = Handlebars.compile(source)
      content.innerHTML = template(data);
      
        $.each(data.places, function (index, value){
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
          clickMarker(bubble.id);
        })

        $('#content-nav').append(bubble);
      
        var address = data.places[index]["gsx$place"]["$t"] + ",Los Angeles, CA";
        gc.geocode( { 'address' : address}, function(results, status) {
          if (status == google.maps.GeocoderStatus.OK) {
            loc = new google.maps.LatLng(results[0].geometry.location.lat(), results[0].geometry.location.lng());
            console.log(loc);
          }

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

      // $("#content").append(cardTemp({apidata: data}));
      $.each(data.places, function (index, value){
        mapMarkers[mapMarkers.length] = new google.maps.Marker({
          position: gc.geocode( { 'address' : 'University of California, Los Angeles, CA' }),
          map: map,
          draggable: false,
          animation: google.maps.Animation.DROP,
          title: value["title"],
          icon: normalPinURL
      });

      var markerIndex = mapMarkers.length-1;
      // google.maps.event.addListener(mapMarkers[markerIndex], 'click', function() {
      //   clickPin(markerIndex);
      // });

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