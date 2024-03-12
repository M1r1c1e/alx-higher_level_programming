#!/usr/bin/node
const fs = require('fs');
const ContentfileA = fs.readFileSync(process.argv[2], 'utf8');
const ContentfileB = fs.readFileSync(process.argv[3], 'utf8');
const result = ContentfileA + ContentfileB;

fs.writeFileSync(process.argv[4], result);
