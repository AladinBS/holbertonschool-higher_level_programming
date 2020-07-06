#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
function fct (arr, i) {
  request(arr[i], function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      const n = JSON.parse(body).name;
      console.log(n);
      if (i + 1 < arr.length) {
        fct(arr, i + 1);
      }
    }
  });
}
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (let j = 0; j < results.length; j++) {
      if (results[j].url === `${url}${filmId}/`) {
        const characters = results[j].characters;
        fct(characters, 0);
      }
    }
  }
});
