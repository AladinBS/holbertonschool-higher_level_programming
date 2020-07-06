#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  fs.writeFile(process.argv[4], '', { flag: 'wx' }, (err) => {
    if (err) {
      throw err;
    }
  });
  fs.readFile(process.argv[2], (err, data) => {
    if (err) {
      throw err;
    } else {
      fs.appendFile(process.argv[4], data, (err) => {
        if (err) {
          throw (err);
        }
      });
    }
  });
  fs.readFile(process.argv[3], (err, data) => {
    if (err) {
      throw err;
    } else {
      fs.appendFile(process.argv[4], data, (err) => {
        if (err) {
          throw (err);
        }
      });
    }
  });
}
