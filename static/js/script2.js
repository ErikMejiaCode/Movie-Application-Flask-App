const API_KEY = "api_key=6ab065a08b162fcedfff0b12d13dd9e4";
const BASE_URL = "https://api.themoviedb.org/3";
const API_URL = BASE_URL + '/movie/616820/reviews?' + API_KEY + '&language=en-US&page=1';
const IMG_URL = 'https://image.tmdb.org/t/p/w500';

const main = document.querySelector('#main')
const resultsDiv = document.querySelector("#movie_1")
const results = document.querySelector("#video")

// Details Javascript

fetch('https://api.themoviedb.org/3/movie/616820?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US')
    .then(res => res.json())
    .then(data => {
        console.log(data)
        resultsDiv.innerHTML = '';
        resultsDiv.innerHTML =
            `
            <div id="movie_1">
                <div class="left">
                    <img src="${IMG_URL + data.poster_path}">
                    <div class="movie-info">
                        <h3>${data.title}</h3>
                        <span class="${getColor(data.vote_average)}">${data.vote_average}</span>
                    </div>
                </div>
                <div class="right">
                    <div class="overview">
                        <h3>${data.overview}</h3>
                    </div>
                    <h5>Release Date: ${data.release_date}</h5>
                    <h5>Runtime: ${data.runtime} minutes</h5>
                    <h5>Status: ${data.status}</h5>
                    <h5>Budget: ${data.budget}</h5>
                    <h5>Popularity: ${data.popularity}</h5>
                    <h5>Vote Count: ${data.vote_count}</h5>
                    <h5>Genres: ${data.genres[0].name}, ${data.genres[1].name}</h5>
                    <div class="trailer">
                        Movie Trailer
                    </div>
                </div>
            </div>
            `
    }
    )

function getColor(vote) {
    if (vote >= 8) {
        return 'green'
    } else if (vote >= 5) {
        return 'orange'
    } else {
        return 'red'
    }
}

function createIframe(video) {
    const iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube.com/embed/i_mAWKyfj6c';
    iframe.width = 360;
    iframe.height = 320;
    iframe.allowFullscreen = true;
    return iframe;
}
fetch('https://api.themoviedb.org/3/movie/616820/videos?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US')
    .then(res => res.json())
    .then((data) => {
        console.log('videos: ', data);
        const videos = data.results;
        const length = videos.length > 2 ? 2 : videos.length;
        const iframeContainer = document.createElement('div');

        for (let i = 0; i < length; i++){
            const video = videos[i];
            const iframe = createIframe(video);
            iframeContainer.appendChild(iframe);
            trailer.appendChild(iframe);
        }
    })
    .catch((error) => {
        console.log('Error', error);
    });




getReviews(API_URL)

function getReviews(url) {
    fetch(url).then(res => res.json()).then(data => {
        console.log(data)
        showReviews(data.results);
    })
}

function showReviews(data) {

    main.innerHTML = '';
    data.forEach(review => {
        const { author, content, rating, created_at, updated_at, author_details } = review;
        const movieEL = document.createElement('div')
        movieEL.classList.add('review');
        movieEL.innerHTML = `
            
            <div class="user">
                <p>Name: ${author}</p>
                <p>Rating: ${author_details['rating']}</p>
                <p>Created at: ${created_at}</p>
                <p>Updated at: ${updated_at}</p>
            </div>
            <div class="user_review">
                <div class="review_text">
                    ${content}
                </div>
            </div>
            `
        main.appendChild(movieEL);
    });
}

//Fetch testing - not used in final product
// fetch('https://api.themoviedb.org/3/movie/616820/reviews?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US&page=1')
//     .then(res => res.json())
//     .then(data => {
//         console.log(data)
//         main.innerHTML = '';
//         main.innerHTML = 
//             `
//             <div class="review">
//             <div class="user">
//             <p>UserName: ${data.author}</p>
//             <p>Rating: ${data.rating}</p>
//             <p>Created at: ${data.created_at}</p>
//             <p>Updated at: ${data.updated_at}</p>
//             </div>
//             <div class="user_review">
//             <div class="review_text">
//                 ${data.content}
//             </div>
//             </div>
//             </div>
//             `
//     });

