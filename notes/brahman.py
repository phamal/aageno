#!/usr/bin/python
import urllib2
import bs4
import json
import sys
import glob
import os

from elasticsearch import  Elasticsearch


def indexNote(note):
    es = Elasticsearch(['http://159.203.66.191:9200'])
    res = es.index(index="brahman", doc_type='note', id=note["maintag"], body=note)
    print(note["maintag"]+" Backup: "+str(res['created'])


def noteBackUps():
    helpdir = '/apps/code/aageno/scripts/help/'
    files = glob.glob(helpdir + "*.txt")

    for file in files:
        note = {}
        note["maintag"] = os.path.splitext(os.path.basename(file))[0]
        note["body"] = open(file,'r').read()
        indexNote(note)

def main():
    noteBackUps()

main()
