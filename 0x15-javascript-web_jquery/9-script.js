const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.ajax({
  type: 'GET',
  url: url,
  success: function (data) {
    $('DIV#hello').text(data.hello);
  }
});
