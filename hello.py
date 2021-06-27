# running the flasker in development environment
# in GITBASH terminal
# export FLASK_ENV=development
# export FLASK_APP=hello.py
# this listens for changes
# flask run --> runs a baby webserver comes with flask

from flask import Flask, render_template

# Create a flask instance
# helps flask finds all the directories
app = Flask(__name__)

# Create a route decorator
# few list of JINJA 2 filters
# --> safe, capitalize, lower, upper, title, trim, striptags


@app.route('/')  # index route
def index():
    # heading tag
    # render templates from the template folder
    # should be in the same work env
    first_name = 'Antarip'
    stuff = "This is <strong>BOLD</strong> text"
    strip_tags = 'This is a <strong>stripped tag</strong> text'
    favourite_players = ["Rafael Nadal", "Cristiano Ronaldo",
                         "Roger Federer", 37]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           striptags=strip_tags,
                           favourite_players=favourite_players)

# Create another route : user/name
# localhost:500/user/Antarip


@app.route('/user/<name>')
def user(name):
    # heading tag
    return render_template("user.html", user_name=name)

# Custom Error Pages


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
