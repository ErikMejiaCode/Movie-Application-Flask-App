import mysql.connector
from flask_app import app;
import requests
from flask import render_template, redirect, session, flash, request
from flask_app.models.users_model import User;
from flask_app.models.reviews_model import Review;
from flask_app.models.movies_model import Movie;
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# route used to display information on one movie / seconds as a post route to add movies into db
@app.route('/movies/<id>', methods=['POST'])
def view_one(id):
    movie = requests.get("https://api.themoviedb.org/3/movie/" + id + "?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    cast = requests.get("https://api.themoviedb.org/3/movie/" + id + "/credits?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    trailer = requests.get("https://api.themoviedb.org/3/movie/" + id + "/videos?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    trailerInfo = trailer.json()
    movieInfo = movie.json()
    castInfo = cast.json()
    
    data = {
        "title" : movieInfo['title'],
        "external_movie_id": movieInfo['id'],
    }

    movie = Movie.create(data)
    return render_template("view_one.html", id = id, castInfo = castInfo, movieInfo = movieInfo, trailerInfo = trailerInfo, movie=movie)


@app.route('/toprated')
def toprated():
    return render_template('top_rated.html')


@app.route('/popular')
def popular():
    return render_template('popular_movies.html')


@app.route('/comingsoon')
def comingsoon():
    return render_template('coming_soon.html')

@app.route('/movies/<id>/reviews')
def movie_reviews(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Eriknay352!@",
        database="movies_website"
    )
    cursor = connection.cursor()

    query = "SELECT * FROM reviews WHERE movie_id=%s"
    cursor.execute(query, (id,))
    result = cursor.fetchall()

    reviews = []
    for review in result:
        reviews.append({
            'username': review[1],
            'content': review[2],
            'rating': review[3]
        })
    
    return render_template('movie_review.html', reviews=reviews)