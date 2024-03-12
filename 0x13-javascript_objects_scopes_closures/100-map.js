#!/usr/bin/node
// a script that imports an array and computes a new array

const list = require('./100-data.js').list;
const newList = list.map((element, index) => element * index);

console.log(list);
console.log(newList);
