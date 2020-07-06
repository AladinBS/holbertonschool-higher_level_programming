const $ = window.$;
const url = 'https://www.fourtonfish.com/hellosalut/?lang=';

function getHello () {
  const search = $('INPUT#language_code').val();
  $.ajax({
    type: 'GET',
    url: url + search,
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
}

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    getHello();
  });
  $('INPUT#language_code').keypress(function (e) {
    if (e.keyCode === 13) {
      getHello();
    }
  });
});
