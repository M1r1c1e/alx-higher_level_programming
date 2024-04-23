#!/usr/bin/node
// script that gets the contents of a webpage 

const request = require('request');
const file_str = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    file_str.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
