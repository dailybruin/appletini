$(document).ready(function() {
  $('#slides').superslides({
    hashchange: true
  });

  $(window).scroll(function() {
  	if ($('#navbar').offset().top > 100) {
  		$('#navbar').addClass('scrolled');
  	}
  	else {
  		$('#navbar').removeClass('scrolled');
  	}
  })
});