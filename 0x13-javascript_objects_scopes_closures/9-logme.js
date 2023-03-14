#!/usr/bin/node

exports.logMe = function (item) {
  if (typeof this.i === 'undefined') {
    this.i = 0;
  }
  console.log(this.i + ': ' + item);
  this.i++;
};
