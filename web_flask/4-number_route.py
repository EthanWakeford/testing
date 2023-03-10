#!/usr/bin/python3
'''flask application setup'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    '''prints hello HBHB'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_hbnb():
    '''prints HBHB'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
    '''prints text'''
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hbnb_python(text='is cool'):
    '''prints text'''
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def hbnb_number(n):
    '''prints the number if its a number'''
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
