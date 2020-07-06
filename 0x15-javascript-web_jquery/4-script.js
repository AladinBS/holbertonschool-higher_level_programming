const $ = window.$;
$('DIV#toggle_header').click(function () {
  if ($('HEADER').hasClass('green')) {
    $('HEADER').toggleClass('green');
    $('HEADER').toggleClass('red');
  } else {
    $('HEADER').toggleClass('red');
    $('HEADER').toggleClass('green');
  }
});
