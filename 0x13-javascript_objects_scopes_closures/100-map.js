#!/usr/bin/node

exList = require('./100-data').list;
const newList = list.map(function (num, index) {
  return num * index;
})

console.log(list);
console.log(newList);
