#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
