from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
class Review:
    db = "movie_review_db"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.rating = data['rating']
        self.date_watched = data['date_watched']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM reviews JOIN users ON reviews.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        reviews = []
        for row in results:
            review = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'email': row['email'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            user = User(user_data)
            review.user = user
            reviews.append(review)
        return reviews

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM reviews JOIN users ON reviews.user_id = users.id WHERE reviews.id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        review = cls(row)
        user_data = {
            'id': row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'age': row['age'],
            'email': row['email'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        user = User(user_data)
        review.user = user
        return review

    @classmethod
    def save(cls, data):
        query = "INSERT INTO reviews(title, content, rating, date_watched, user_id) VALUES(%(title)s, %(content)s, %(rating)s, %(date_watched)s, %(user_id)s);"
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, age = %(age)s WHERE id = %(id)s;"
        user_id = connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        user_id = connectToMySQL(cls.db).query_db(query, data)

