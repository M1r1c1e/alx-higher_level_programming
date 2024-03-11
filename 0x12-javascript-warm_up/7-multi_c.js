#!/usr/bin/node
const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 0; n < num; n++) {
    console.log('C is fun');
  }
}
