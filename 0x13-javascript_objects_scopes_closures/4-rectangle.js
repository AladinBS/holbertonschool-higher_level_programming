#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

Rectangle.prototype.print = function () {
  for (let i = 0; i < this.height; i++) {
    for (let j = 0; j < this.width; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
};

Rectangle.prototype.rotate = function () {
  const temp = this.height;
  this.height = this.width;
  this.width = temp;
};

Rectangle.prototype.double = function () {
  this.height = this.height * 2;
  this.width = this.width * 2;
};

module.exports = Rectangle;
