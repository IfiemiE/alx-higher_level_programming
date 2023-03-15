#!/usr/bin/node

let nb = 0;
exports.logMe = function (arg) {
  nb++;
  console.log(`${nb}: ${arg}`);
};
