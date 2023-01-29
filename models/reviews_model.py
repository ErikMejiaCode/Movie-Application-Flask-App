from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import users_model


class Review:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.content = data["content"]
        self.rating = data["rating"]
        self.user_id = data["user_id"]
        self.movie_id = data["movie_id"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO reviews (content, rating, user_id, movie_id)"\
            "VALUES (%(content)s, %(rating)s, %(user_id)s, %(movie_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE reviews SET content = %(content)s, user_id = %(user_id)s, movie_id = %(movie_id)s"\
            "WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM reviews WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM reviews JOIN users ON reviews.user_id = users.id WHERE reviews.movie_id = %(movie_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            all_reviews = []
            for row in results:
                this_review = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']

                }
                this_user = users_model.User(user_data)
                this_review.planner = this_user
                all_reviews.append(this_review)
            return all_reviews
        return []

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM reviews JOIN users ON reviews.user_id = users.id WHERE reviews.id = %(id)s AND reviews.movie_id = %(movie_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_review = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        this_user = users_model.User(user_data)
        this_review.planner = this_review
        return this_review 

    @staticmethod
    def validator(form_data):
        is_valid = True;

        if len(form_data['rating']) < 1:
            flash("Rating required")
            is_valid = False

        if len(form_data['content']) < 1:
            flash("Tell us more before submitting your review")
            is_valid = False;

        return is_valid;