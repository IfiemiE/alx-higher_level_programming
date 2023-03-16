#!/usr/bin/node

const dict = require('./101-data').dict;

const dictKeys = Object.keys(dict);
const dictValues = Object.values(dict);

let newKeys = new Set(dictValues);
newKeys = Array.from(newKeys);

let newDict = {};
for (let k = 0; k < newKeys.length; k++) {
  const key = newKeys[k];
  const value = [];
  for (let i = 0; i < dictKeys.length; i++) {
    if (dict[dictKeys[i]] === key) {
      value.push(dictKeys[i]);
    }
  }
  newDict = { ...newDict, [key]: value };
}

console.log(newDict);
