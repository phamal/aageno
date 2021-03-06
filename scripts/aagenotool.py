#!/usr/bin/python
import json
import requests
import csv
import sys, getopt
import subprocess
import glob
import os
import configparser

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
        else:
            print("Usage: %s -d input -s output" % sys.argv[0])

    if status != '':
        if status == 'all':
            monitorAll(domain)
        else:
            print "Type what status you want to see. statuses {elasticsearch }"
    elif action != '':
        if action == 'stocks':
            stocksDownload(domain)
        if action == "downloadlib":
            downloadLib(domain)
        if action == "startcore":
            startCore(domain)
        if action == "stopcore":
            stopCore(domain)
        if action == 'backupnotes':
            backUpNotes(domain)
        if action == 'restartes':
            restartElasticsearchIfNeeded(domain)
        if action == 'restartcoreifstopped':
            restartCoreIfNeeded(domain)
        if action == 'restartcore':
            stopCore(domain)
            startCore(domain)
        if action == 'startview':
            startView(domain)
        else:
            print "Type what action to perform. actions : {stocks | dowanloadlib | startcore " \
                  " | backupnotes | restartes | restartcore | restartcoreifstopped}"

    elif helptopic != '':
        helpdir = getSysConfig('aageno_app','aagenoBase')+'/scripts/help/'
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






def getSysConfig(section,key):
    config = configparser.ConfigParser()
    config.read('/etc/aageno/data.ini')
    return config[section][key]

def getUrlResponseJson(url):
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
            return True
        else:
            printError("Error : Elasticsearch  is not running")
            return False

    except IOError:
        printError("Error connecting aageno elasticsearch")

def monitorFlaskApp(domain):
    try:
        flaskApp = "http://159.203.66.191:5000/test"

        response = getUrlResponse(flaskApp)
        if response.status_code == 200:
            printSuccess("Aaageno is running")
        else:
            printError("Aaagento is running")

    except IOError:
        printError("Error connecting aageno main app")


def monitorAll(domain):
    print "******CHECKING VARIOUS STATUSES*******"
    monitorElasticSearch(domain)
    monitorFlaskApp(domain)

def stocksDownload(domain):
    os.chdir(getSysConfig('aageno_app','aagenoBase')+'/extractor/')
    runAndPrintCommand(['./main.py'])

def downloadLib(domain):
    os.chdir(getSysConfig('aageno_app','aagenoBase')+'/scripts/')
    runAndPrintCommand(['./pyd.sh'])

def backUpNotes(domain):
    os.chdir(getSysConfig('aageno_app','aagenoBase')+'/notes/')
    runAndPrintCommand(['./brahman.py'])

def startCore(domain):
    os.chdir(getSysConfig('aageno_app','aagenoBase')+'/core/')
    runAndPrintCommand(['./main.py'])

def stopCore(domain):
    killProcessesInPort('5000')

def startView(domain):
    os.chdir(getSysConfig('aageno_app','aagenoBase')+'/view/quickstart/')
    runAndPrintCommand(['npm','start'])


def restartElasticsearchIfNeeded(domain):
    running = monitorElasticSearch(domain)
    if running:
        print('Es already running')
    else:
        print('service elasticsearch start')
        runCommand(['service','elasticsearch','start'])

def restartCoreIfNeeded(domain):
    running = monitorFlaskApp(domain)
    if running:
        print('Aaageno is running')
    else:
        print('Starting aageno app')
        startCore(domain)

def killProcessesInPort(port):
    for processid in processInPort(port):
        print "Port : "+str(port) +" Process : " + str(processid);
        subprocess.call(['kill',processid])

def processInPort(port):
    from subprocess import Popen, PIPE
    p1 = Popen(['lsof', '-i', ':'+str(port)], stdout=PIPE)
    processids = []
    for line in iter(p1.stdout.readline, ''):
        substrs = str.split(line);
        if(substrs[1].isdigit()):
             processids.append(substrs[1])

    return processids

def runCommand(command):
    subprocess.Popen(command, stdout=subprocess.PIPE)

def runCommandAndReturnOutput(command):
    action = subprocess.Popen(command, stdout=subprocess.PIPE)
    return action.communicate()[0]

def runAndPrintCommand(command):
    action = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = action.communicate()[0]
    print output

############ Actions ##############################





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
