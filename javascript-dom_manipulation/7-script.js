fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())

.then(data => {
    data.results.forEach(movie => {
      const title = document.createElement('li');
      title.textContent = movie.title;
      document.querySelector('#list_movies').appendChild(title);
    });
  })