#!/usr/bin/node
const Square = require('./5-square');

class SquareC extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = SquareC;
