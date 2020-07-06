#!/usr/bin/node

module.exports.converter = function (base) {
  function convertToBase (n) {
    return n.toString(base);
  }
  return convertToBase;
};
