from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.review import Review

@app.route('/movie_dashboard')
def movie_dashboard():
    data = {
        'id': session['id']
    }
    return render_template("movie_dashboard.html", reviews=Review.get_all(), user=User.get_one(data))

@app.route('/reviews/create', methods=['POST'])
def create_review():
    Review.save(request.form)
    return redirect('/movie_dashboard')

@app.route('/reviews/<int:id>')
def show_review(id):
    user_data = {
        'id': session['id']
    }

    review_data = {
        "id": id
    }
    return render_template("show_review.html", review=Review.get_one(review_data), user=User.get_one(user_data))
