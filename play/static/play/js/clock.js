var SU = SU || {};

$(document).ready(function() {
  // Initialize the module when the page loads.
  SU.Timer.init();
});

SU.Timer = function () {
  var clock = $('.js-clock');

  var toggleTimer = function (clock) {
    // Initialize the play/pause button of the timer.
    var icon = $('.js-timer-control');
    var button = $('.play-button');
    button.on('click', function() {
      if ($('.js-timer-control').hasClass('pause')) {
        clock.timer('pause');
      }
      else {
        clock.timer('resume');
      }
      icon.toggleClass('pause');
      icon.toggleClass('play');
      button.toggleClass('btn-success');
      button.toggleClass('btn-warning');
    });
  };

  var resetTimer = function () {
    // To reset the timer, remove it then add it back.
    clock.timer('remove').timer();
  };

  return {
    init: function () {
      clock.timer();
      toggleTimer(clock);
    },
    resetTimer: resetTimer
  };
}();
