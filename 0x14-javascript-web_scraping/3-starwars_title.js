#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  const filmId = process.argv[2];
  const url = 'https://swapi-api.hbtn.io/api/films/' + filmId;
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}
