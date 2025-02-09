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


@app.route("/c/<text>", strict_slashes=False)
def c_route(text: str = None) -> str:
    """
    Route that displays 'C ' followed by the value of 'text'.

    Args:
        text (str); The input message.

    Returns:
        str: A formatted message.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text: str = "is cool") -> str:
    """
    Route that displays 'Python ' followed by the value of 'text'.

    Args:
        text (str); The input message.

    Returns:
        str: A formatted message.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n: int) -> str:
    """
    Route that displays a message indicating the input is a number.

    Args:
        n (int); The input number.

    Returns:
        str: A formatted message indicating that n is a number.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
