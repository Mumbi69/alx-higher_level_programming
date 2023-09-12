#!/usr/bin/node
class Square {
  constructor(size) {
    this.width = size;
    this.height = size;
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

class SquareWithCharPrint extends Square {
  constructor(size) {
    super(size);
  }
}

module.exports = SquareWithCharPrint;
