import mysql.connector
from flask_app import app
import requests
from flask import render_template, redirect, request, session, flash
from flask_app.models.users_model import User
from flask_app.models.reviews_model import Review
from flask_app.models.movies_model import Movie


@app.route('/reviews/<id>')
def see_reviews(id):
    if 'user_id' not in session:
        return redirect('/')
    r = requests.get("https://api.themoviedb.org/3/movie/" + id + "?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    movieInfo = r.json()
    user_data = {
        'id': session['user_id']
    }
    movie_data = {
        'movie_id': id
    }
    logged_user = User.get_by_id(user_data)
    all_reviews = Review.get_all(movie_data)
    return render_template("reviews.html", movieInfo=movieInfo, id=id, logged_user=logged_user, all_reviews=all_reviews)


@app.route('/reviews/<id>/new')
def new_review(id):
    if 'user_id' not in session:
        return redirect('/')
    r = requests.get("https://api.themoviedb.org/3/movie/" + id +
    "?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    movieInfo = r.json()
    print("hello there")
    return render_template('new_review.html', movieInfo=movieInfo, id=id)


@app.route('/reviews/<id>/create', methods=['POST'])
def create_review(id):
    if 'user_id' not in session:
        return redirect('/')

    if not Review.validator(request.form):
        return redirect(f'/reviews/{id}/new')

    external_movie_id = id
    movie = requests.get(
        f"https://api.themoviedb.org/3/movie/{external_movie_id}?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    movie_info = movie.json()

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Eriknay352!@",
        database="movies_website"
    )
    cursor = connection.cursor()

    query = "SELECT id FROM movies WHERE external_movie_id=%s"
    cursor.execute(query, (external_movie_id,))
    result = cursor.fetchone()

    if not result:
        pass

    movie_id = result[0]
    data = {
        **request.form,
        'user_id': session['user_id'],
        'movie_id': movie_id
    }
    Review.create(data)
    return redirect(f'/movies/{id}/reviews')


@app.route('/movies/<id>/reviews')
def movie_review(id):
    if not 'user_id' in session:
        return redirect('/')
    user_data = {
        'id' : session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    all_reviews = Review.get_all
    print(all_reviews)
    return render_template('movie_review.html', logged_user=logged_user, all_reviews=all_reviews)


@app.route('/reviews/<movie_id>/<id>/delete')
def delete_review(movie_id, id):
    if 'user_id' not in session:
        return redirect('/')
    r = requests.get("https://api.themoviedb.org/3/movie/" + id + "?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    movieInfo = r.json()
    Review.delete({'id': id})
    return redirect(f'/reviews/{movie_id}', movieInfo=movieInfo)
