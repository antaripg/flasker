from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField # Field and Submit button for the forms
from wtforms.validators import DataRequired # Validation check for the string field


# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key_for_flasker" # csrf token

# Create a Form Class

class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")




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

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html", name=name, form=form)
