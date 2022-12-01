#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let string = '';
      for (let w = 0; w < this.height; w++) {
        for (let h = 0; h < this.width; h++) {
          string += c;
        }
        if (w !== this.height - 1) {
          string += '\n';
        }
      }

      console.log(string);
    }
  }
}

module.exports = Square;
