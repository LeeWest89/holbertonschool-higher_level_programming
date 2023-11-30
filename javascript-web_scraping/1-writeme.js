#!/usr/bin/node
// write and prints the contents of a file
const fs = require('fs');
const fp = process.argv[2];
const words = process.argv[3];

fs.writeFile(fp, words, 'utf-8', (e) => {
  if (e) {
    console.error(e);
  }
});
