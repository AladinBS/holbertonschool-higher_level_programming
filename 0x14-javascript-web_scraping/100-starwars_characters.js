#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    for (let i = 0; i < result.characters.length; i++) {
      request(result.characters[i], function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
