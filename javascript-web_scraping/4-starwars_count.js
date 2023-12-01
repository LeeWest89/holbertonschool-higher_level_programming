#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const req = require('request');
const url = process.argv[2];

req(url, (e, response, data) => {
  if (e) {
    console.error(e);
  } else {
    const movies = JSON.parse(data).results;
    const characterCount = movies.filter(movie => movie.characters.some(character => character.includes('/people/18/')));
    console.log(characterCount.length);
  }
});
