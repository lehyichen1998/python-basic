'''

'''

from flask import Flask

app = Flask(__name__)


@app.route("/")
def first():
    return 'Hello World!!!!'


@app.route("/")
def eat():
    return '我正在吃饭!!!'


@app.route("/sleep")
def sleep():
    return '我正在睡觉!!!'


app.run()
