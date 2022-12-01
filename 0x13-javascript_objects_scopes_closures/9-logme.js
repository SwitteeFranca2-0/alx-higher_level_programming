#!/usr/bin/node

let funcCall = 0;
exports.logMe = function (item) {
  console.log(funcCall + ': ' + item);
  funcCall++;
};
