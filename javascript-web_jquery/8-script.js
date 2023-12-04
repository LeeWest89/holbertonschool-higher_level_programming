#!/usr/bin/node
// fetches and lists the title for all movies by using the URL
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (key, film) {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  });
});
