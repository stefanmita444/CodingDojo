from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "movie_review_db"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            user = cls(row)
            users.append(user)
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

    @classmethod
    def get_one_with_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, age) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(age)s);"
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

