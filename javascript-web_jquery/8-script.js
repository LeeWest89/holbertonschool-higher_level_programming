#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data){
  $('UL#list_movies').append(...data.results.map(film => `<li>${film.title}</li>`));
});
