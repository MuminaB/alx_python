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

"""run the app on required ip and port"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
