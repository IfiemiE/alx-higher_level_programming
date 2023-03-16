#!/usr/bin/node

let n = 0;
function nbOccurence (x) {
  const r = n * x;
  n++;
  return (r);
}

const list = require('./100-data').list;

const newList = list.map(nbOccurence);

console.log(list);
console.log(newList);
