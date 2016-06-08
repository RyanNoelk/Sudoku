var SU = SU || {};

SU.Message = function () {
  var bg = $(".js-bg");

  // Display a message right under the header
  var displayMessage = function (msg_type) {
    clearMessage();
    if (msg_type == 'ok') {
      $(".js-message-warning").show();
      bg.addClass('bg-warning');
    }
    else if (msg_type == 'problem') {
      $(".js-message-danger").show();
      bg.addClass('bg-danger');
    }
    else if (msg_type == 'complete') {
      $(".js-message-success").show();
      bg.addClass('bg-success');
    }
    else if (msg_type == 'new') {
      $(".js-message-default").show();
      bg.addClass('bg-primary');
    }
    else {
      $(".js-message-error").show();
      bg.addClass('bg-danger');
    }
  };

  // Hide all messages and remove the background color
  var clearMessage = function () {
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
    displayMessage: displayMessage
  };
}();
