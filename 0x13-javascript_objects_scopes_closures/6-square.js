#!/usr/bin/node

const Squ = require('./5-Square');

class Square extends Squ {
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
