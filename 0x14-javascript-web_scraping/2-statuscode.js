#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  const url = process.argv[2];
  request.get(url).on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
}
