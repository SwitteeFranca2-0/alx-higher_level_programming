#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let w = 0; w < this.height; w++) {
      for (let h = 0; h < this.width; h++) {
        string += 'X';
      }
      if (w !== this.height - 1) {
        string += '\n';
      }
    }

    console.log(string);
  }
}

module.exports = Rectangle;
