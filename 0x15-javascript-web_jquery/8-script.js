#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  movies = data.results;
  movies.forEach(movie => {
    title = movie.title;
    $('UL#list_movies').append(`<li> ${title} </li>`);
  });
});
