#!/usr/bin/node

exports.converter = function (base) {
  function baseN (num) {
    return (num.toString(base));
  }
  return baseN;
};
