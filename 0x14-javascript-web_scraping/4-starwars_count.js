#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let numFilms = 0;
request.get(url, function (error, response, body) {
  if (error) throw error;
  const infoList = JSON.parse(body).results;
  for (let i = 0; i < infoList.length; i++) {
    if (infoList[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) { numFilms += 1; }
  }
  console.log(numFilms);
});
