#!/usr/bin/node

const arr = require('./100-data').list;

const newArr = arr.map((currentVal, idx) => currentVal * idx);

console.log(arr);
console.log(newArr);
