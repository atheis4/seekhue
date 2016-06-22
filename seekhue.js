'use strict';

/**
defines the interactive elements on my web app
*/
function registerEventHandlers() {
  // shows the hidden form div on click of form button
  $('#show-form').on('click', function() {
    var formDiv = $('#form-div');
    formDiv.fadeIn();
  });

  // hides the form div on click of form 'X'
  $('#form-exit').on('click', function() {
    var formDiv = $('#form-div');
    formDiv.fadeOut();
  });

  // changes the source of the target image to the sorted-image path
  $('img').on('mouseover', function(event) {
    var seekhueSortSrc = $(event.target).attr('data-sort-src');
    $(event.target).attr('src', seekhueSortSrc);
  });

  // changes the src of the target image back to the original-image path
  $('img').on('mouseout', function() {
    var originalSrc = $(event.target).attr('data-orig-src');
    $(event.target).attr('src', originalSrc);
  });

  // changes css properties of link text and background on mouseover
  $('.nav-link').on('mouseover', function(event) {
    $(event.target).css('background-color', 'rgba(255, 255, 255, .75)');
    $(event.target).css('color', 'black');
  });

  // changes css properties of link back to default on mouseout
  $('.nav-link').on('mouseout', function(event) {
    $(event.target).css('background-color', 'rgba(0, 0, 0, .5)');
    $(event.target).css('color', 'white');
  });

  // changes css properties of search button on mouseover
  $('.search-button').on('mouseover', function(event) {
    $(event.target).css('background-color', 'lightgreen');
    $(event.target).css('color', 'white');
  });

  // changes css properties of search button back to default on mouseout
  $('.search-button').on('mouseout', function(event) {
    $(event.target).css('background-color', 'white');
    $(event.target).css('color', 'black');
  });
}

$(document).ready(registerEventHandlers);
