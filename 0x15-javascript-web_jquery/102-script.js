const $ = window.$;
const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const search = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: url + search,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
