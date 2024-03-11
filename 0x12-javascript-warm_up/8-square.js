#!/usr/bin/node
const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let sym = '';
    for (let i = 0; i < num; i++) {
      sym += 'X';
    }
    console.log(sym);
  }
}
