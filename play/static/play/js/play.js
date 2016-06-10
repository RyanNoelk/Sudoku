var SU = SU || {};

$(document).ready(function() {
  // Initialize the module when the page loads.
  SU.Play.init();
}).ajaxStart(function() {
  // Add the loading class when an ajax event occurs.
  $(".js-sudoku_board").addClass('loading');
}).ajaxStop(function() {
  // Remove the loading class when an ajax event occurs.
  $(".js-sudoku_board").removeClass('loading');
});

SU.Play = function () {
  var ajax = function (action, callback) {
    $.get({
      url: "/api/",
      data: {
        action: action,
        puzzle: getPuzzle(),
        difficulty: $('.js-difficulty-text').html()
      },
      type: "GET",
      dataType : "json",
      success : callback,
      error: checkMessage
    })
  };

  // Display a message when a user requests there puzzle to be checked
  var checkMessage = function (json) {
    SU.Message.displayMessage(json.result)
  };

  // Reload the HTML of the current board with a new one.
  var refreshBoard = function(json) {
    SU.Message.displayMessage('new');
    $("#board").html(json.board_html);
    SU.Timer.resetTimer();
  };

  // Change the difficulty of the puzzle
  var ChangeDifficulty = function(difficulty) {
    // TODO: Check if the puzzle has been worked on
    // If it has, ask the user if they want to abandoned there current game
    
    // Change the difficulty dropdown and refresh the board
    $(".js-difficulty-text").html(difficulty);
    ajax('new', refreshBoard);
  };

  // Get the current puzzle and return it as a json string (array of arrays)
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
        ajax('check', checkMessage);
      });
      $('.js-new').on('click', function () {
        ajax('new', refreshBoard);
      });
      $('.js-difficulty').on('click', function () {
        ChangeDifficulty($(this).html());
      });
      $('.js-reset').on('click', function () {
        $( "input" ).each(function() {
          $( this ).val('');
        });
        SU.Timer.resetTimer();
      });
    }
  };
}();
