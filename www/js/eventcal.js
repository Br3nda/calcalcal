

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
    });
}
