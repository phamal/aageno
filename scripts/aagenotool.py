#!/usr/bin/python
import json
import requests
import csv
import sys, getopt
import subprocess
import glob
import os
import re
import time
import sh
import xml


DPX_TEST_URL = ""
NOTIFICATION_TEST_URL = ""



# Status URLS ###



def getUrlResponseJson(url):
    # url = "http://dev.bidsync.com:9380/bidsync-business-provider/rs/batch/mailgunDeliveryStatuses"

    response = requests.get(url)

    json_obj = json.loads(response.text)

    return json_obj


def getUrlResponse(url):
    response = requests.get(url)
    return response


def writeListToCSV():
    myfile = open('testresults.csv', 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    # wr.writerow(mylist)


def monitorApis():
    print "Checking the statuses of the apis -- "



def runNotificationTestSuite():
    print "Running notification test automation --- "



def printError(msg):
    print bcolors.FAIL + msg + bcolors.ENDC


def printSuccess(msg):
    print bcolors.OKGREEN + msg + bcolors.ENDC


def monitorElasticSearch(domain):
    try:
        ELASTICSEARCH = "http://159.203.66.191:9200"

        response = getUrlResponse(ELASTICSEARCH)
        json_obj = json.loads(response.text)
        status_code = json_obj["status"]
        if status_code == 200:
            printSuccess("Elasticsearch is running")
        else:
            printError("Error : Elasticsearch  is not running")

    except IOError:
        printError("Error connecting aageno elasticsearch")


def monitorAll(domain):
    print "******CHECKING VARIOUS STATUSES*******"
    monitorElasticSearch(domain)



############# Actions ###########################
def stocksDownload(domain):
    runCommand(['cd', '/apps/code/aageno/extractor/'])
    runAndPrintCommand(['./main.py'])

def downloadLib(domain):
    runCommand(['cd', '/apps/code/aageno/scripts/'])
    subprocess.call(['./pyd.sh'])

def runCommand(command):
    subprocess.Popen(command, stdout=subprocess.PIPE)

def runCommandAndReturnOutput(command):
    action = subprocess.Popen(command, stdout=subprocess.PIPE)
    return action.communicate()[0]

def runAndPrintCommand(command):
    action = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = action.communicate()[0]
    print output

def startAll(domain,parameter):
    os.chdir('/apps/code/bidsync')

    print "ant dist"
    #runAndPrintCommand(['ant','dist'])

    print "wft bidsync undeploy"
    runAndPrintCommand(['wft','bidsync','undeploy'])
    print "wft bidsync stop"
    runAndPrintCommand(['wft', 'bidsync', 'undeploy'])
    print "wft bidsync start"
    runAndPrintCommand(['wft', 'bidsync', 'undeploy'])
    print "wft bidsync deploy"
    runAndPrintCommand(['wft', 'bidsync', 'deploy'])



############ Actions ##############################


def main():
    myopts, args = getopt.getopt(sys.argv[1:], "d:s:a:p:h:t:")

    domain = 'dev'
    action = ''
    status = ''
    parameter = ''
    helptopic = ''
    anttestfile = ''
    for o, a in myopts:
        if o == '-d':
            domain = a
        elif o == '-s':
            status = a
        elif o == '-a':
            action = a
        elif o == '-h':
            helptopic = a
        elif o == '-t':
            anttestfile = a
        elif o == '-p':
            try:
                parameter = json.loads(a)
            except ValueError:
                parameter = a;
        else:
            print("Usage: %s -d input -s output" % sys.argv[0])

    if status != '':
        if status == 'all':
            monitorElasticSearch(domain)
        else:
            print "Type what status you want to see. statuses {elasticsearch }"
    elif action != '':
        if action == 'stocks':
            stocksDownload(domain)
        if action == "downloadlib":
            downloadLib(domain)
        else:
            print "Type what action to perform. actions : {stocks | dowanloadlib | runreport | sshaageno | portprocess | kill | killport}"

    elif helptopic != '':
        helpdir = '/apps/code/aageno/scripts/help/'
        if helptopic == 'options' or helptopic == '':
            files =  glob.glob(helpdir+"*.txt")
            count = 0;
            line = ""
            for file in files:
                print os.path.splitext(os.path.basename(file))[0]


        else:
            if helptopic.find(".") == -1:
                file = helpdir + helptopic + '.txt';
            else:
                file = helpdir + helptopic;

            subprocess.call(['vi', file])




    else:
        print "Looks like you need some help. -h helptopics"




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


main()
