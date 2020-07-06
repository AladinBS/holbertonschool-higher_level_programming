#!/usr/bin/node

let count = 0;
module.exports.logMe = function (item) {
  process.stdout.write(count + ': ' + item + '\n');
  count += 1;
};
