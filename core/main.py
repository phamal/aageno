#!/usr/bin/python

from flask import request
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
import requests
from elasticsearch import  Elasticsearch
from flask_cors import CORS, cross_origin
import logging


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:kurakai@localhost/aageno'
db = SQLAlchemy(app)

@app.route("/",methods=['GET', 'POST'])
def index():
    searchString = ""
    if request.method == 'POST':
       searchString = request.form['searchString']
    elif request.method == "GET":
       searchString = request.args.get("searchString", "")

    notes = []
    if(len(searchString) > 0):
        note = {}
        es = Elasticsearch(['http://159.203.66.191:9200'])
        searchString = searchString.strip();
        if searchString.startswith("#"):
            tag = searchString[1:len(searchString)]
            res = es.get(index="brahman", doc_type='note', id=tag)
            note["title"] = tag;
            note["body"] = res['_source']['body']
            notes.append(note)
        else:
            res = es.search(index="brahman", doc_type="note", body={"query": {"match": {"body": searchString}}})
            returnString = ""
            for hit in res['hits']['hits']:
                note = {}
                note["title"] = str(hit["_id"])
                notestr = str(hit["_source"]['body'])
                note["body"] = notestr
                notes.append(note)

    return render_template("index.html",notes = notes);

@app.route("/addNote")
def addNote():
    app.logger.error("Adding note")
    return render_template("index.html");


@app.route("/test")
def test():
    return "Restarting core as part of the CI"

@app.route("/stocks")
def stocksList():
    company = {}
    return "Show all of the stocks"

@app.route("/notes",methods=['GET', 'POST'])
def notes():
    es = Elasticsearch(['http://159.203.66.191:9200'])
    searchString = request.args.get("key","")
    res = es.search(index="brahman", doc_type="note", body={"query": {"match": {"body": searchString}}})
    ##res = es.search(index="test-index", body={"query": {"match_all": {}}})
    returnString = ""
    for hit in res['hits']['hits']:
        title = str(hit["_id"])
        note = str(hit["_source"]['body'])
        note = "<br />".join(note.split("\n"))
        note = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".join(note.split("\t"))
        returnString +=  "<div style='border:1px solid #000;padding:10px; margin-bottom:30px;'> <b>"+title+"</b><br>"+note+"</div>"
    return returnString

@app.route('/api/addNote', methods=['POST'])
def addNoteApi():
    print "Khai k ho ta hit gareko ho ta"
    app.logger.info("ggg "+str(request.get_json(force=True)))
    note = {}
    note["title"] = "Title Added"
    note["body"] = "Body added"
    return jsonify(note);

@app.route('/api/note/<tag>')
def getNote(tag):
    es = Elasticsearch(['http://159.203.66.191:9200'])
    res = es.get(index="brahman", doc_type='note', id=tag)
    note = {}
    noteBody = res['_source']['body']
    #note["body"] = noteBody;
    noteBody = "<br />".join(noteBody.split("\n"))
    note["body"] = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".join(noteBody.split("\t"))
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

