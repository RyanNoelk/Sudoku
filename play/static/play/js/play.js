var SU = SU || {};

$(document).ready(function() {
  // Initialize the module when the page loads
  SU.Play.init();
});

SU.Play = function () {
  var ajax = function (action) {
    $.get({
      url: "/api/",
      data: {
        action: action,
        puzzle: getPuzzle()
      },
      type: "GET",
      dataType : "json"
    })
    .success(function( json ) {
      if (json.output == 'False') {
        $(".js-alert-error").show();
      }
      else {
        $(".js-alert-error").show();
      }
    })
    .fail(function( xhr, status, errorThrown ) {
      console.log( "Error: " + errorThrown );
      console.log( "Status: " + status );
      console.dir( xhr );
      $(".js-alert-error").show();
    })
    .always(function( xhr, status ) {
      console.log( "The request is complete!" );
    });
  };

  var getPuzzle = function () {
    var puzzle = [], row = [];
    $('.js-cell').each(function(index) {
      var val = $(this).text();
      if (val == '') {
        val = $(this).val();
        if (val == '') {
          val = 0;
        }
      }
      row.push(parseInt(val));
      //TODO: make this dynamic
      if ((index+1) % 9 == 0) {
        puzzle.push(row);
        row = []
      }
    });
    
    return JSON.stringify(puzzle);
  };

  return {
    init: function () {
      $('.js-check').on('click', function () {
        ajax('check');
      });
      $('.js-reset').on('click', function () {
        location.reload();
      });
    }
  };
}();
