'use strict';

var submitLink = $('#show-form');

$(submitLink).on('click', function() {
  var formDiv = $('#form-div');
  formDiv.fadeIn();
});

var formCloseLink = $('#form-exit');

$(formCloseLink).on('click', function() {
  var formDiv = $('#form-div');
  formDiv.fadeOut();
});


var imgEls = $('img');

$(imgEls).on('mouseover', function(event) {
  var seekhueSortSrc = $(event.target).attr('data-sort-src');
  $(event.target).attr('src', seekhueSortSrc);
});

$(imgEls).on('mouseout', function() {
  var originalSrc = $(event.target).attr('data-orig-src');
  $(event.target).attr('src', originalSrc);
});


var navLinkEls = $('.nav-link');

$(navLinkEls).on('mouseover', function(event) {
  $(event.target).css('background-color', 'rgba(255, 255, 255, .75)');
  $(event.target).css('color', 'black');
});

$(navLinkEls).on('mouseout', function(event) {
  $(event.target).css('background-color', 'rgba(0, 0, 0, .5)');
  $(event.target).css('color', 'white');
});


var searchButtonEl = $('.search-button');

$(searchButtonEl).on('mouseover', function() {
  $(searchButtonEl).css('background-color', 'lightgreen');
  $(searchButtonEl).css('color', 'white');
});

$(searchButtonEl).on('mouseout', function() {
  $(searchButtonEl).css('background-color', 'white');
  $(searchButtonEl).css('color', 'black');
});
