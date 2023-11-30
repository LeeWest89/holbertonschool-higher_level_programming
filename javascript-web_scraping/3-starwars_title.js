#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const req = require('request');
const num = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${num}/`;

req(url, (e, response, data) => {
  if (e) {
    console.error(e);
  } else {
    const movie = JSON.parse(data);
    console.log(movie.title);
  }
});
