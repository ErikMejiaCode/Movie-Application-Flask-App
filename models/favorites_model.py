from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import users_model
from flask_app.models import movies_model

class Favorite:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.movie_id = data["movie_id"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
