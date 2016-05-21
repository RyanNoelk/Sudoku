var SU = SU || {};

$(document).ready(function() {
  // Initialize the module when the page loads
  SU.play.init();
});

SU.play = function () {
  return {
    init: function () {
      $('td').on('click', function () {
        //$(this).html("<input class='js-select' type='text'>")
      });
    }
  };
}();
