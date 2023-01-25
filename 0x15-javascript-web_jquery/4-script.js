#!/usr/bin/node

if ($('header').is(':empty') == false) {
  if ($('header')[0].classList.length == 1) {
    $('#toggle_header').click(function () {
      $('header').toggleClass('red green');
    });
  }
}
