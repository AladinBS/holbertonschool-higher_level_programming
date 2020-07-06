#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  const url = process.argv[2];
  let count = 0;
  const actor = '/api/people/18/';
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const results = JSON.parse(body).results;
      for (let i = 0; i < results.length; i++) {
        const charUrls = results[i].characters;
        if (charUrls.find(el => el.includes(actor))) {
          count++;
        }
      }
      console.log(count);
    }
  });
}
