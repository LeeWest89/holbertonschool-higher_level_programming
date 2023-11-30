#!/usr/bin/node
// display the status code of a GET request.
const req = require('request');
const url = process.argv[2];

req(url, (e, data) => {
  if (e) {
    console.error(e);
  } else {
    console.log(`code: ${data.statusCode}`);
  }
});
