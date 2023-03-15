#!/usr/bin/node

let nb = 0;
exports.logMe = function (arg) {
  console.log(`${nb}: ${arg}`);
  nb++;
};
