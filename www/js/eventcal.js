

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
	console.log(response);
	
	$('#section-calendar').empty().append('<h2>Today</h2>');
	
	for (i in response['today']) {
	    e = response['today'][i];
	    $('#section-calendar').append(event_markup(e));
	}
	
	$('#section-calendar').append('<h2>This Month</h2>');
	for (i in response['this_month']) {
	    e = response['this_month'][i];
	    $('#section-calendar').append(event_markup(e));
	}

	$('#section-calendar').append('<h2>' + response['next_month_name'] + '</h2>');
	for (i in response['next_month']) {
	    e = response['next_month'][i];
	    $('#section-calendar').append(event_markup(e));
	}
    });
}

function event_markup(e) {
  return ' \
    <div class="line-item"> \
	    <span class="day">' + e['dow'] + '</span> \
	    <span class="date">' + e['day']  +'</span> \
	    <span class="time">' + e['time'] + '</span> \
	    <span class="group"><a href="#">' + e['group'] + '</a></span> \
	    <span class="event">' + e['name'] + '</span> \
	    <span class="location">' + e['location'] + '</span> \
    </div> \
    ';
}
