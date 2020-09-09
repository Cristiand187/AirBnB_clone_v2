#!/usr/bin/python3
"""
script that starts a Flask web application
application must be listening on 0.0.0.0, port 5000
"""
from flask import render_template
from flask import Flask
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """/: display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display “HBNB”"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_txt(text):
    """/c/<text>: display “C” followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_txt(text="is cool"):
    """/python/(<text>): display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space )"""
    text = text.replace("_", " ")
    return "python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """/number/<n>: display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """/number_template/<n>: display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """/number_odd_or_even/<n>: display a HTML page only if n is an integer:"""
    return render_template("6-number_odd_or_even.html", n=n)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    /states_list: display a HTML page: (inside the tag BODY)
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    /cities_by_states: display a HTML page: (inside the tag BODY)
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """/states: display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """/hbnb_filters: display a HTML page like 6-index.html, which was done
    during the project 0x01. AirBnB clone - Web static"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """
    /states_list: display a HTML page: (inside the tag BODY)
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
