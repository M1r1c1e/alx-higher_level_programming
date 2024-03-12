#!/usr/bin/node
const squareRef = require('./5-square');

class Square extends squareRef {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let sym = '';
        for (let r = 0; r < this.width; r++) {
          sym += c;
        }
        console.log(sym);
      }
    }
  }
}

module.exports = Square;
