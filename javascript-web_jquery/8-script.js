#!/usr/bin/node
// fetches and lists the title for all movies by using the URL
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(film => `<li>${film.title}</li>`));
});
