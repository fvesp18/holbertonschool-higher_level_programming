#!/usr/bin/node
$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/' + '?lang=' + $('#language_code').val(),
      function (data) {
        $('#hello').text(data.hello);
      });
  });
  $('#language_code').focus(function () {
    $('#language_code').keypress(function (event) {
      if (event.keyCode === 13) {
        $.get('https://fourtonfish.com/hellosalut/' + '?lang=' + $('#language_code').val(),
          function (data) {
            $('#hello').text(data.hello);
          });
      }
    });
  });
});
