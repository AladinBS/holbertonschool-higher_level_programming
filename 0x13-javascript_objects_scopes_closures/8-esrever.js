#!/usr/bin/node

module.exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList[list.length - i - 1] = list[i];
  }
  return reversedList;
};
