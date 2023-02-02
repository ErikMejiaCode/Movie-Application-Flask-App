//API used - TMDB- The Movie DB

//Grabbing ID from URL to use in API call for cast information 
var movieURL = window.location.href
var movieID = movieURL.substring(movieURL.lastIndexOf('/') + 1);

const API_KEY = "api_key=6ab065a08b162fcedfff0b12d13dd9e4";
const BASE_URL = "https://api.themoviedb.org/3";
const API_URL = BASE_URL + '/movie/now_playing?' + API_KEY + '&language=en-US&page=1';
const Cast_URL = BASE_URL + '/movie/' + movieID + '/credits?' + API_KEY + '&language=en-US';
const Movie_URL = BASE_URL + '/movie/' + movieID + '?' + API_KEY + '&language=en-US'
const Review_URL = BASE_URL + '/movie/' + movieID + '/reviews?' + API_KEY + '&language=en-US&page=1'
const Videos_URL = BASE_URL + '/movie/' + movieID + '/videos?' + API_KEY + '&language=en-US'
const Base_Youtube = 'https://www.youtube.com/embed/';
const IMG_URL = 'https://image.tmdb.org/t/p/w500';

const main = document.getElementById('main')
const cast_information = document.getElementById("cast_information");
const movie_details = document.getElementById("movie_details");
const review_text = document.getElementById("review_text");

// Dashboard javascript
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
            <form action="/movies/${id}" method="post" class="form">
                <button class="btn btn-sm btn-info"><a id="image_click" href="/movies/${id}"><img src="${IMG_URL + poster_path}" alt='${title}'></a></button>
            </form>
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


//Javascript for One movie - Actors
getActors(Cast_URL)

function getActors(url) {
    fetch(url).then(res => res.json().then(data => {
        console.log(data.cast)
        showActors(data.cast)
    }))
}
function showActors(data) {

    cast_information.innerHTML = '';

    data.slice(0, 7).forEach(actor => {

        const { character, name, profile_path } = actor;
        const actorEl = document.createElement('div');
        actorEl.classList.add('actor_card');
        actorEl.innerHTML = `
        
        <img src="${IMG_URL + profile_path}" alt="${name}">
                <div class="actor_name">
                    <h5><strong>${character}</strong></h5>
                    <p>${name}</p>
                </div> 
        
        `
        cast_information.appendChild(actorEl);
    });
}

//Javascript for One Movie - Reviews
getReviews(Review_URL)

function getReviews(url) {
    fetch(url).then(res => res.json().then(data => {
        console.log(data.results)
        showReviews(data.results)
    }))
}
function showReviews(data) {

    review_text.innerHTML = '';

    data.slice(0, 10).forEach(review => {

        const { author, created_at, url, content, author_details } = review;
        const reviewElement = document.createElement('div');
        reviewElement.classList.add('review');
        reviewElement.innerHTML = `
        
        <div class="review">
            <div class="user">
                <p>Written by: ${author}</p>
                <p>Rating: ${author_details.rating}/10 </p>
                <p>Date: ${created_at.slice(0, 10)} </p>
            </div>
            <div class="user_review">
                <div class="review_text">
                    ${content}
                </div>
            </div>
            <div class="review_url">
                <p>Review Source: <a href="${url}" target="_blank">${url}</a> </p>
            </div>
        </div>
        
        `
        review_text.appendChild(reviewElement);
    });
}


// Javascript to show YouTube video trailers for movies 
fetch(Videos_URL).then((response) => {
    return response.json();
}).then((data) => {
    let trailers = data.results.filter(video => video.type === "Trailer");
    if (trailers.length) {
        let videoId = trailers[0].key;
        let iframe = `<iframe width='100%'height="91.5%" src="https://www.youtube.com/embed/${videoId}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`
        document.getElementById('video-container').innerHTML = iframe;
    } else {
        console.log("No Trailer Available")
    }
});





