from flask import Flask, request, render_template, flash, redirect, url_for, abort
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

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Validate the data: ensure both fields are provided
        if not name or not email:
            flash('Please provide both name and email.')
            return render_template('update_user.html')

        user = User.query.get(user_id)

        if user:
            # Update the user's name and email
            user.name = name
            user.email = email

            try:
                db.session.commit()
                flash('User updated successfully!')

            except Exception as e:
                db.session.rollback()
                flash(f'An error occurred. {e}')
        else:
            flash(f'No user with id {user_id} found.')

    # For GET requests, render the update_user.html template
    return render_template('update_user.html')

##updating a user

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'GET':
        user = User.query.get(user_id)
        if not user:
            flash('User not found')
            return redirect(url_for('index'))
        return render_template('update_user.html', user=user)
    elif request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if not name or not email:
            flash('Name and email are required')
            return redirect(url_for('update_user', user_id=user_id))
        user = User.query.get(user_id)
        if not user:
            flash('User not found')
            return redirect(url_for('index'))
        user.name = name
        user.email = email
        try:
            db.session.commit()
            flash('User updated successfully')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occurred: {e}')
            return redirect(url_for('update_user', user_id=user_id))
    return None

##deleting a user

@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    db.session.delete(user)
    try:
        db.session.commit()
        flash('User deleted successfully')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'An error occurred: {e}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
     
