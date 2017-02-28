#!/usr/bin/python

from flask import request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
import requests
from elasticsearch import  Elasticsearch

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:kurakai@localhost/aageno'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello aageno"

@app.route("/test")
def test():
    return "Restarting core as part of the CI"

@app.route("/stocks")
def stocksList():
    company = {}
    return "Show all of the stocks"

@app.route("api/notes")
def notes():
    note = {}
    note["body"] = "Note Body"
    note["title"] = "Note Title"
    return jsonify(note);


@app.route("/note/<tag>")
def hashtagNote(tag):
    es = Elasticsearch(['http://159.203.66.191:9200'])
    res = es.get(index="brahman", doc_type='note', id=tag)
    note = res['_source']['body']
    note = "<br />".join(note.split("\n"))
    note = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".join(note.split("\t"))

    return note


if __name__ == "__main__":
    app.run(host='0.0.0.0')

