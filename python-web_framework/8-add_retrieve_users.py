from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"

db = SQLAlchemy(app) #to initialize sqlalchemy

class User(db.Model):
    # Define columns for the user’s ID (as an integer and primary key), name, and email
    # Both name and email should be of type string
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Define a __repr__ method to show a user object
    def __repr__(self):
        return f"<User {self.name}>"


# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    # For POST requests
    if request.method == 'POST':
        # Retrieve name and email from the submitted form data
        name = request.form.get('name')
        email = request.form.get('email')

        try:
            # Create a new user object with the name and email
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()
            flash('User added successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred. {e}')

    return render_template('add_user.html')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
     
