#!/usr/bin/node
// function that read from file

const file_con = require('fs');
file_con.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
