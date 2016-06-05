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
  var originalSrc = $(event.target).attr('src');
  var seekhueSortSrc = $(event.target).attr('data-sort-src');
  $(event.target).attr('src', seekhueSortSrc);

  $(imgEls).on('mouseout', function() {
    $(event.target).attr('src', originalSrc);
  });
});
