from flask_app import app;
import requests
from flask import render_template, redirect, session, flash, request
from flask_app.models.users_model import User;
from flask_app.models.reviews_model import Review;
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# route used to display information on one movie
@app.route('/movies/<id>')
def view_one(id):
    movie = requests.get("https://api.themoviedb.org/3/movie/" + id + "?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    cast = requests.get("https://api.themoviedb.org/3/movie/" + id + "/credits?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")
    trailer = requests.get("https://api.themoviedb.org/3/movie/" + id + "/videos?api_key=6ab065a08b162fcedfff0b12d13dd9e4&language=en-US")

    trailerInfo = trailer.json()
    movieInfo = movie.json()
    castInfo = cast.json()
    print(movieInfo)
    print(castInfo)
    return render_template("view_one.html", id = id, castInfo = castInfo, movieInfo = movieInfo, trailerInfo = trailerInfo)


@app.route('/toprated')
def latest():
    if not 'user_id' in session:
        return redirect('/')
    user_data = {
        'id' : session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('top_rated.html', logged_user=logged_user)


@app.route('/popular')
def popular():
    if not 'user_id' in session:
        return redirect('/')
    user_data = {
        'id' : session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('popular_movies.html', logged_user=logged_user)


@app.route('/comingsoon')
def comingsoon():
    if not 'user_id' in session:
        return redirect('/')
    user_data = {
        'id' : session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('coming_soon.html', logged_user=logged_user)