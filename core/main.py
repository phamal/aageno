#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/stocks")
def stocksList():
    return "Show all of the stocks"


if __name__ == "__main__":
    app.run()

