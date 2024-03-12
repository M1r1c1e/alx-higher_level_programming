#!/usr/bin/node
// defining a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let sym = '';
      for (let r = 0; r < this.width; r++) {
        sym += 'X';
      }
      console.log(sym);
    }
  }
}

module.exports = Rectangle;
