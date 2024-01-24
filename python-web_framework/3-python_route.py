"""
Script that starts a flask web application
"""

from flask import Flask

"""An instance of Flask"""
app = Flask(__name__)

"""route for '/' """
@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

"""Route for '/hbnb'"""
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

"""route for '/c/<text>'"""
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "C " + text

"""route for '/python/<text>'"""
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return "Python " + text

"""run the app on required ip and port"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
