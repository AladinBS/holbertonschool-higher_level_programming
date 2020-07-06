const $ = window.$;
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    if ($('UL.my_list')[0].childElementCount > 0) {
      $('UL.my_list')[0].lastElementChild.remove();
    }
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
