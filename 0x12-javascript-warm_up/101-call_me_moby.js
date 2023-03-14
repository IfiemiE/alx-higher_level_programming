#!/usr/bin/node

function callMeMoby (x, myFunc) {
  for (let i = 0; i < x; i++) {
    myFunc();
  }
}
module.exports = { callMeMoby };
