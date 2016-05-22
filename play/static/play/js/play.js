var SU = SU || {};

$(document).ready(function() {
  // Initialize the module when the page loads
  SU.Play.init();
});

SU.Play = function () {
  var ajax = function () {
  $.ajax({
    url: "/api/",
    data: {
      action: 123,
      puzzle: getPuzzle()
    },
    type: "GET",
    dataType : "json"
  })
    .success(function( json ) {
      alert( json );
    })
    .fail(function( xhr, status, errorThrown ) {
      alert( "Sorry, there was a problem!" );
      console.log( "Error: " + errorThrown );
      console.log( "Status: " + status );
      console.dir( xhr );
    })
    .always(function( xhr, status ) {
      alert( "The request is complete!" );
    });
  };

  var getPuzzle = function () {
    return 1
  };

  return {
    init: function () {
      $('.js-check').on('click', function () {
        ajax()
      });
    },
  };
}();
