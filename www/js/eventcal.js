

function get_events() {
  var jqxhr = $.ajax( "/api/events.json" )
    .done(function() { 
      console.log(jqxhr);
    })
    .fail(function() {
      
    })
    .always(function() { 
      
    });
}



function page_setup() {
    get_next_events();
}

function get_next_events() {
    $.ajax({
        url: "/api/events.json",
        context: document.body
    }).done(function(response) {
	$('#section-calendar').empty().append('<h2>Today</h2>');
	
	for (i in response['today']) {
	    e = response['today'][i];
	    console.log(e);
	    $('#section-calendar').append(event_markup(e));
	}
    });
}

function event_markup(e) {
  event = ' \
    <div class="line-item"> \
	    <span class="day">Tu</span> \
	    <span class="date">4</span> \
	    <span class="time">6:30pm</span> \
	    <span class="group"><a href="#">Creative Skills</a></span> \
	    <span class="event">The Smell of Ink in the Morning</span> \
	    <span class="location">The Kitchen</span> \
    </div> \
    ';
    return event
}
