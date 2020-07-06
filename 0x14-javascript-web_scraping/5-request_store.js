#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length === 4) {
  const url = process.argv[2];
  const fileName = process.argv[3];

  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      fs.writeFile(fileName, body, 'utf-8', (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}
