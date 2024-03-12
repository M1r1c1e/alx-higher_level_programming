#!/usr/bin/node
// defining a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

// print rectangle using x
  print () {
    for (let i = 0; i < this.height; i++) {
      let sym = '';
      for (let r = 0; r < this.width; r++) {
        sym += 'X';
      }
      console.log(sym);
    }
  }

//  multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }

// exchanges the width and the height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = Rectangle;
