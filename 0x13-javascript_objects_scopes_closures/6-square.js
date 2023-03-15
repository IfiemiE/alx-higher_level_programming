#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let pen = '';
      for (let j = 0; j < this.width; j++) {
        pen += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(pen);
      }
    }
  }
}

module.exports = Square;
