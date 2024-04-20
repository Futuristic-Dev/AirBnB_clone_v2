#!/usr/bin/python3

"""
A script that starts a Flask web application.

The web application must listen on 0.0.0.0, port 5000.
Routes:
    - /: display "Hello HBNB!"
    - /hbnb: display "HBNB"
    - /c/<text>: display "C" followed by the value of the text variable
"""

import flask as flask
app = flask.Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Display 'Hello HBNB!' in the route '/'."""
    return "Hello HBNB!"

def hbnb():
    """Display 'HBNB' in the route '/hbnb'."""
    return "HBNB"

def display_c(text):
    """Display 'C' followed by the value of the text variable."""
    return "C {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)