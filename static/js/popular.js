//API used - TMDB- The Movie DB

//Grabbing ID from URL to use in API call for cast information 
var movieURL = window.location.href
var movieID = movieURL.substring(movieURL.lastIndexOf('/') + 1);

const API_KEY = "api_key=6ab065a08b162fcedfff0b12d13dd9e4";
const BASE_URL = "https://api.themoviedb.org/3";
const API_URL = BASE_URL + '/movie/popular?' + API_KEY + '&language=en-US';

const IMG_URL = 'https://image.tmdb.org/t/p/w500';

const main = document.getElementById('main')

// Latest javascript
getMovies(API_URL)

function getMovies(url) {
    fetch(url).then(res => res.json()).then(data => {
        console.log(data.results)
        showMovies(data.results);
    })
}
function showMovies(data) {

    main.innerHTML = '';
    data.forEach(movie => {
        const { title, poster_path, vote_average, overview, id } = movie;
        const movieEL = document.createElement('div')
        movieEL.classList.add('movie');
        movieEL.innerHTML = `
            <a id="image_click" href="/movies/${id}"><img src="${IMG_URL + poster_path}" alt='${title}'></a>
            <div class="movie-info">
                <h3>${title}</h3>
                <span class="${getColor(vote_average)}">${vote_average}</span>
            </div>
            <div class="overview">
                ${overview}
            </div>
            `
        main.appendChild(movieEL);
    });
}

function getColor(vote) {
    if (vote >= 8) {
        return 'green'
    } else if (vote >= 5) {
        return 'orange'
    } else {
        return 'red'
    }
}