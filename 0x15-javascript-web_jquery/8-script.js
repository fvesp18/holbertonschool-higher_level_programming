#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const title in data.results) {
    $('#list_movies').append('<li>' + data.results[title].title + '</li>');
  }
});
