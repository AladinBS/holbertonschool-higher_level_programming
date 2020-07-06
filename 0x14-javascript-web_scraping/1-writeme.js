#!/usr/bin/node

const fs = require('fs');
if (process.argv.length === 4) {
  const fileName = process.argv[2];
  const data = process.argv[3];
  fs.writeFile(fileName, data, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
}
