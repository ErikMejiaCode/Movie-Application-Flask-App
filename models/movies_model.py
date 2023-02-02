from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import users_model
from flask_app.models import reviews_model

class Movie:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.title = data['title']
        self.external_movie_id = data["external_movie_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def create(cls, data):
        query = "INSERT INTO movies (title, external_movie_id) VALUES (%(title)s, %(external_movie_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)