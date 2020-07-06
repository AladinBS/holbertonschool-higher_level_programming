const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $filmList = $('UL#list_movies');
$.ajax({
  type: 'GET',
  url: url,
  success: function (data) {
    console.log(data);
    $.each(data.results, function (i, film) {
      $filmList.append(`<li>${film.title}</li>`);
    });
  }
});
