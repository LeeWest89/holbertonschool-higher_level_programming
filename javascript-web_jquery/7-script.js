#!/usr/bin/node
// fetches the character name from the URL
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
