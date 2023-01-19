#!/usr/bin/node

const request = require('request');

const dataDic = {};
request.get('https://jsonplaceholder.typicode.com/todos', function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body);
  for (let i = 1; i < 11; i++) {
    let sum = 0;
    for (let b = 0; b < data.length; b++) {
      if (data[b].userId === i && data[b].completed === true) { sum += 1; }
    }
    dataDic[i] = sum;
  }
  console.log(dataDic);
});
