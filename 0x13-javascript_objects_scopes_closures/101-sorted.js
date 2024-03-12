#!/usr/bin/node
const dict = require('./101-data.js').dict;

const key = {};

for (const val in dict) {
  const count = dict[val];
  if (count in key) {
    key[count].push(val);
  } else {
    key[count] = [val];
  }
}
console.log(key);
