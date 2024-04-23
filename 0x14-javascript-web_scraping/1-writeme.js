#!/usr/bin/node

const file_open = require('fs');

file_open.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (err) {
    if (err) {
      console.log(err);
    }
  });
