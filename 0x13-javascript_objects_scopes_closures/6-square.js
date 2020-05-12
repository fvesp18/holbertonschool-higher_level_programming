#!/usr/bin/node
const PSquare = require('./5-square.js');
module.exports = class Square extends PSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
      let row = 0;
      let col = 0;
      let str = '';
      for (; row < this.height; row++) {
        for (; col < this.width; col++) {
          str += c;
        }
        console.log(str);
      }
    } else {
      let row = 0;
      let col = 0;
      let str = '';
      for (; row <= this.height - 1; row++) {
        for (; col <= this.width - 1; col++) {
          str += c;
        }
        console.log(str);
      }
    }
  }
};
