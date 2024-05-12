from flask import Flask, render_template



# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator

# Index Route
@app.route("/")
def index():
    first_name = "John"
    test_sentence = "This is <strong>bold</strong> text"
    favorite_pizza = ['peperoni', 'cheese', 'Mushroom', 42]
    return render_template("index.html",
    first_name=first_name,
    test=test_sentence,
    favorite_pizza=favorite_pizza)


# User Name Route
@app.route("/user/<name>")
def user_name(name):
    return render_template("user.html", user_name=name)

# Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404 # This is syntax


# Internal Server Error URL
@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500 # This is syntax
