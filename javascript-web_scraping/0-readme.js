#!/usr/bin/node
// reads and prints the contents of a file
const fs = require('fs');
const fp = process.argv[2];

fs.readFile(fp, 'utf-8', (e, data) => {
  if (e) {
    console.error(e);
  } else {
    console.log(data || "");
  }
});
