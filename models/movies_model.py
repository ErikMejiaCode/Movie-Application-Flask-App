from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import users_model
from flask_app.models import reviews_model

class Movie:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]