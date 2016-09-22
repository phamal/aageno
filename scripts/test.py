#!/usr/bin/python


import json
import requests
import csv
import sys, getopt

DPX_TEST_URL = ""
NOTIFICATION_TEST_URL = ""
domain = ""
status = ""


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


def monitorNotification(domain):
    response = None
    try:
        NOTIFICATION = "http://" + domain + ".bidsync.com:9480/notification-web/rs/test/notificationMessagesTableForToday"
        print NOTIFICATION
        response = getUrlResponse(NOTIFICATION)

        statuscode = response.status_code;
        if statuscode == 200:
            printSuccess("Notification app is running")
            ##print "Round robin table of the day : " + response.text
        else:
            printError("Notification app is not deployed. Need to deploy notification app. -- wft notification deploy")

    except IOError:
        printError("Error connecting to notification app. Need to start the app -- wft notification start")


def monitorDPX(domain):
    response = None
    try:
        DPX = "http://" + domain + ".bidsync.com:9180/dpx/rs/general/test"
        print DPX
        response = getUrlResponse(DPX)

        statuscode = response.status_code;
        if statuscode == 200:
            printSuccess("DPX app is running")
        else:
            printError("DPX app is not deployed. Need to deploy dpx app. -- wft dpx deploy")

    except IOError:
        printError("Error connecting to dpx app. Need to start the app -- wft dpx start")


def runNotificationTestSuite():
    print "Running notification test automation --- "


def monitorJMS(domain):
    try:
        JMS = "http://" + domain + ".bidsync.com:9480/notification-web/rs/test/testjms"
        response = getUrlResponse(JMS)

        if response.text == "success":
            printSuccess("JMS in notification is running")
        else:
            printError("Error : jms in notification is not running")

    except IOError:
        printError("Error connecting to notification app. Need to start the app -- wft notification start")


def monitorRef(domain):
    try:
        REF = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/test/running"

        response = getUrlResponse(REF)

        statuscode = response.status_code;
        if statuscode == 200:
            printSuccess("Refactor is running")
        else:
            printError("Refactor is not deployed. Need to deploy refactor. -- wft bidsync deploy")

    except IOError:
        printError("Error connecting to refactor. Need to start the app -- wft refactor start")


def monitorRefactorBatches(domain):
    print "Check statuses of the refactor batches"


def monitorDpxBathes(domain):
    print "Check statuses of the dpx batches"


def printError(msg):
    print bcolors.FAIL + msg + bcolors.ENDC


def printSuccess(msg):
    print bcolors.OKGREEN + msg + bcolors.ENDC


def monitorCas(domain):
    print "Monitoring cas "


def monitorElasticSearch(domain):
    try:
        ELASTICSEARCH = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/test/elasticsearch"

        response = getUrlResponse(ELASTICSEARCH)
        json_obj = json.loads(response.text)
        status_code = json_obj["status"]
        if status_code == 200:
            printSuccess("Elasticsearch in notification is running")
        else:
            printError("Error : Elasticsearch  is not running")

    except IOError:
        printError("Error connecting to refactor Need to start the app -- wft notification start")


def monitorSmartProcure(domain):
    try:
        SMARTPROCURE = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/test/smartprocureurl"
        response = getUrlResponse(SMARTPROCURE)
        if(response.text.find('app.smartprocure.us') != -1):
            printSuccess("Smartprocure is running")


    except IOError:
        printError("Error connecting to refactor Need to start the app -- wft notification start")


def monitorTax(domain):
    try:
        SMARTPROCURE = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/test/salestax"
        response = getUrlResponse(SMARTPROCURE)
        json_obj = json.loads(response.text)
        print json_obj

    except IOError:
        printError("Tax integration is failing")


def monitorMuhimbi(domain):
    print "Muhimbi status --- "


def monitorBlueSnap(domain):
    print "Muhimbi bluesnap --- "


def monitorClassifier(domain):
    print "Monitor extractor classifier"

def monitorExtractor(domain):
    print "Monitor extractor"

def monitorMarketo(domain):
    print "Monitor marketo"

def monitorAll(domain):
    monitorDPX(domain)
    monitorRef(domain)
    monitorJMS(domain)
    monitorNotification(domain)
    monitorElasticSearch(domain)
    monitorSmartProcure(domain)
    monitorDpxBathes(domain)
    monitorRefactorBatches(domain)
    monitorCas(domain)
    monitorMuhimbi(domain)
    monitorBlueSnap(domain)
    monitorTax(domain)
    monitorExtractor(domain)
    monitorMarketo(domain)



def main():
    myopts, args = getopt.getopt(sys.argv[1:], "d:s:")

    domain = 'dev'
    for o, a in myopts:
        if o == '-d':
            domain = a
        elif o == '-s':
            status = a
        else:
            print("Usage: %s -d input -s output" % sys.argv[0])
    if status != '':
        if status == 'notification':
            monitorNotification(domain)
        if status == 'ref':
            monitorRef(domain)
        elif status == 'dpx':
            monitorDPX(domain)
        elif status == 'cas':
            monitorCas(domain)
        elif status == 'all':
            monitorAll(domain)
        elif status == 'jms':
            monitorJMS(domain)
        elif status == 'smartprocure':
            monitorSmartProcure(domain);
        elif status == 'elasticsearch':
            monitorElasticSearch(domain)
        elif status == 'tax':
            monitorTax(domain)
        else:
            print "looks like you need some help"


    else:
        print "Looks like you need some help --"


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
