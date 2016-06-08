var SU = SU || {};

$(document).ready(function() {
  // Initialize the module when the page loads
  SU.Play.init();
  SU.Timer.init();
});
$( document ).ajaxStart(function() {
  $(".js-sudoku_board").addClass('loading');
});
$( document ).ajaxStop(function() {
  $(".js-sudoku_board").removeClass('loading');
});

SU.Play = function () {
  var ajax = function (action, callback) {
    $.get({
      url: "/api/",
      data: {
        action: action,
        puzzle: getPuzzle()
      },
      type: "GET",
      dataType : "json",
      success : callback
    })
    .fail(function( xhr, status, errorThrown ) {
      var bg = $(".js-bg");
      clearMessage(bg);
      $(".js-message-error").show();
      bg.addClass('bg-danger');
    })
  };

  var displayCheckMessage = function (json) {
    var bg = $(".js-bg");
    clearMessage(bg);
    if (json.result == 'ok') {
      $(".js-message-warning").show();
      bg.addClass('bg-warning');
    }
    else if (json.result == 'problem') {
      $(".js-message-danger").show();
      bg.addClass('bg-danger');
    }
    else if (json.result == 'complete') {
      $(".js-message-success").show();
      bg.addClass('bg-success');
    }
    else {
      $(".js-message-error").show();
      bg.addClass('bg-danger');
    }
  };

  var refreshBoard = function(json) {
    $("#board").html(json.board_html);
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

  var clearMessage = function (bg) {
    $(".js-message-default").hide();
    $(".js-message-warning").hide();
    $(".js-message-danger").hide();
    $(".js-message-success").hide();
    $(".js-message-error").hide();
    bg.removeClass("bg-warning");
    bg.removeClass("bg-success");
    bg.removeClass("bg-danger");
    bg.removeClass("bg-primary");
  };

  return {
    init: function () {
      $('.js-check').on('click', function () {
        ajax('check', displayCheckMessage);
      });
      $('.js-reset').on('click', function () {
        $( "input" ).each(function() {
          $( this ).val('');
        });
        SU.Timer.resetTimer();
      });
      $('.js-new').on('click', function () {
        ajax('new', refreshBoard);
        SU.Timer.resetTimer();
      });
    }
  };
}();
