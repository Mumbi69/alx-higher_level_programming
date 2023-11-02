$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movieTitles = data.results;

    const $listMovies = $('#list_movies');

    $.each(movieTitles, function(index, movie) {
      $listMovies.append(`<li>${movie.title}</li>`);
    });
  });
});
