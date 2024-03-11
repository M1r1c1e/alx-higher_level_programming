#!/usr/bin/node
const intnum = Number(process.argv[2]);

function factorial (intnum) {
  if (intnum === 0 || isNaN(intnum)) {
    return 1;
  } else {
    return intnum * factorial(intnum - 1);
  }
}
const result = factorial(intnum);
console.log(`${result}`);
