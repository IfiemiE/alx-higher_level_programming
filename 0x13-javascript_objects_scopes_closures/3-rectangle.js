#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let pen = '';
    for (let j = 0; j < this.width; j++) {
      pen += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(pen);
    }
  }
}

module.exports = Rectangle;
