#!/usr/bin/node

const exList = require('./100-data').list;
const newList = exlist.map(function (num, index) {
  return num * index;
})

console.log(exlist);
console.log(newList);
