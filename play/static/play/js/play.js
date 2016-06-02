var SU = SU || {};

$(document).ready(function() {
  // Initialize the module when the page loads
  SU.Play.init();
  $('.js-timer').timer();
  var icon = $('.js-timer-control');
  icon.click(function() {
     icon.toggleClass('pause');
     icon.toggleClass('play');
     return false;
  });
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
      $(".js-alert-blank").hide();
      clearAlerts();
      if (json.result == 'ok') {
        $(".js-alert-warning").show();
      }
      else if (json.result == 'problem') {
        $(".js-alert-danger").show();
      }
      else if (json.result == 'complete') {
        $(".js-alert-success").show();
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

  var clearAlerts = function () {
      $(".js-alert-warning").hide();
      $(".js-alert-danger").hide();
      $(".js-alert-success").hide();
      $(".js-alert-error").hide();
  };

  return {
    init: function () {
      $('.js-check').on('click', function () {
        ajax('check');
      });
      $('.js-reset').on('click', function () {
        location.reload();
      });
      $('.js-close-alert').on('click', function () {
        clearAlerts();
        $(".js-alert-blank").show();
      });
    }
  };
}();
