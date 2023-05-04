$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').wrapInner('<li>Item</li>');
  });
});
