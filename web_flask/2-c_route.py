#!/usr/bin/python3
"""an Flask appilication that great user"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Greet user with 'Hello HBNB' message

    Returns:
        str: A greeting message
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """
    Greet user with 'HBNB' message

    Returns:
        str: A greeting message
    """
    return "HBNB"


@app.route("/hbnb", strict_slashes=False)
def c_route(text):
    """
    Route that displays 'C ' followed by the value of 'text'.

    Args:
        text (str); The input message.

    Returns:
        str: A formatted message.
    """
    return "C {}".format(text.replace("_"," "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
