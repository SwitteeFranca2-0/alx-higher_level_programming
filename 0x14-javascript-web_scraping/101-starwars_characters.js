#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, async function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body).characters;
  for (let i = 0; i < data.length; i++) {
    await new Promise((resolve, reject) => {
      request.get(data[i], function (error, response, body) {
        if (error) throw error;
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
