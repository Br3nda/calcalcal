

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