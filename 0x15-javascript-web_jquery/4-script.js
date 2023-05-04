let i = 1;
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    if ((i % 2) === 0) {
      $('header').addClass('green');
      $('header').removeClass('red');
    } else {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
    i++;
  });
});
