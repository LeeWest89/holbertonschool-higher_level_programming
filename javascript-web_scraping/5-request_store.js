#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const fp = process.argv[3];

req(url, (e, response, data) => {
  if (e) {
	console.error(e);
	return;
  } else {
    fs.writeFile(fp, data, 'utf-8', (e) => {
      if (e) {
        console.error(e);
	  }
	});
  }
});
