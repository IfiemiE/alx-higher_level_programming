#!/usr/bin/node

exports.esrever = function (list) {
  const n = list.length;
  const mid = Math.floor(n / 2);
  if (n > 0) {
    for (let i = 0; i < mid; i++) {
      const swap = list[i];
      list[i] = list[n - i - 1];
      list[n - i - 1] = swap;
    }
  }
  return list;
};
