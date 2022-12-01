#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nmOcc = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      nmOcc += 1;
    }
  }
  return nmOcc;
};
