#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
      let row = 0;
      let col = 0;
      let str = '';
      for (; row < this.width; row++) {
        for (; col < this.height; col++) {
          str += c;
        }
        console.log(str);
      }
    } else {
      let row = 0;
      let col = 0;
      let str = '';
      for (; row <= this.width; row++) {
        for (; col <= this.height; col++) {
          str += c;
        }
        console.log(str);
      }
    }
  }
};
