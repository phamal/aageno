#!/usr/bin/python
import json
import requests
import csv
import sys, getopt
import subprocess
import glob
import os

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


def monitorNotification(domain):
    try:
        NOTIFICATION = "http://" + domain + ".bidsync.com:9480/notification-web/rs/test/notificationMessagesTableForToday"
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
    try:
        DPX = "http://" + domain + ".bidsync.com:9180/dpx/rs/general/test"
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
        print "Notification JMS:"
        response = getUrlResponse(JMS)
        if response.text == "success":
            printSuccess("\tJMS in notification is running")
        else:
            printError("\tError : jms in notification is not running")

    except IOError:
        printError("\tError connecting to notification app. Need to start the app -- wft notification start")


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


def monitorBatches(domain):
    try:
        BATCH_STATUS_API = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/test/batchstatus"
        print "Bach statuses : "
        response = getUrlResponse(BATCH_STATUS_API)
        json_obj = json.loads(response.text)
        for batch in json_obj:
            batchStatus = "\t" + batch['batchType']
            if 'lastRunDate' in batch:
                batchStatus += " | " + str(batch['lastRunDate'])

            if batch['error']:
                batchStatus += " | ERROR "
            else:
                batchStatus += " | SUCCESS "

            if batch['error']:
                printError(batchStatus)
            else:
                printSuccess(batchStatus)
    except IOError:
        printError("Error connecting to refactor Need to start the app -- wft notification start")


def printError(msg):
    print bcolors.FAIL + msg + bcolors.ENDC


def printSuccess(msg):
    print bcolors.OKGREEN + msg + bcolors.ENDC


def monitorElasticSearch(domain):
    try:
        ELASTICSEARCH = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/test/elasticsearch"

        response = getUrlResponse(ELASTICSEARCH)
        json_obj = json.loads(response.text)
        status_code = json_obj["status"]
        if status_code == 200:
            printSuccess("Elasticsearch is running")
        else:
            printError("Error : Elasticsearch  is not running")

    except IOError:
        printError("Error connecting to refactor Need to start the app -- wft bidsync start")


def monitorSmartProcure(domain):
    try:
        SMARTPROCURE = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/test/smartprocureurl"
        response = getUrlResponse(SMARTPROCURE)
        if (response.text.find('app.smartprocure.us') != -1):
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
    try:
        DPX = "http://" + domain + ".bidsync.com:9180/dpx/rs/fileconversion/fileswaitingconversion"
        response = getUrlResponse(DPX)
        parsed = json.loads(response.text)
        print json.dumps(parsed, indent=4, sort_keys=True)
    except IOError:
        printError("Error connecting to dpx app. Need to start the app -- wft dpx start")

def monitorBlueSnap(domain):
    print "Monitor bluesnap --- "


def monitorClassifier(domain):
    print "Monitor extractor classifier ---"


def monitorExtractor(domain):
    print "Monitor extractor ---"


def monitorMarketo(domain):
    print "Monitor marketo ---"


def monitorCas(domain):
    print "Monitoring cas --"


def monitorMailgun(domain):
    print "Monitor mailgun ---"


def monitorNovatus(domain):
    print "Monitor novatus integration ---"


def monitorAll(domain):
    print "******CHECKING VARIOUS STATUSES*******"
    monitorDPX(domain)
    monitorRef(domain)
    monitorJMS(domain)
    monitorNotification(domain)
    monitorElasticSearch(domain)
    monitorSmartProcure(domain)
    monitorBatches(domain)
    monitorCas(domain)
    monitorMuhimbi(domain)
    monitorBlueSnap(domain)
    monitorTax(domain)
    monitorExtractor(domain)
    monitorMarketo(domain)
    monitorClassifier(domain)
    monitorMailgun(domain)
    monitorNovatus(domain)


############# Actions ###########################
def actionDpxNotificationBatch(domain, parameter):
    print "***** Triggering notification batch ******** "
    if not parameter:
        print "Please pass parameter in JSON formmat {'help':true,'run':'continous','args':'all'}"
    else:
        try:
            help = parameter['help']
            run = parameter['run']
            args = parameter['args']
            print help + run + args
            DPX = "http://" + domain + ".bidsync.com:9180/dpx/rs/dpxbatch/notification?continous?help=" + help + "&run=" + run + "&args=" + args
            response = getUrlResponse(DPX)
            print response.text

        except IOError:
            printError("Error connecting to dpx app. Need to start the app -- wft dpx start")


def runbatch(domain, parameter):
    print "********* Running batch ********"
    try:
        URL = ''
        if parameter == 'indexwebbids':
            URL = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/batch/indexWebExtractBids?roundCount=1"
        elif parameter == 'indexauctions':
            URL = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/batch/indexAuctions?roundCount=1"
        elif parameter == 'mailgunstatuses':
            URL = "http://" + domain + ".bidsync.com:9380/bidsync-business-provider/rs/batch/mailgunDeliveryStatuses"
        else:
            print "Unable to identify which batch to run. Here are the parameters : {indexwebbids | indexauctions | mailgunstatuses}"

        if URL != '':
            response = getUrlResponse(URL)
            print "\t Output : " + response.text


    except IOError:
        printError("Error running the batch")


############ Actions ##############################


def main():
    myopts, args = getopt.getopt(sys.argv[1:], "d:s:a:p:h:")

    domain = 'dev'
    action = ''
    status = ''
    parameter = ''
    helptopic = ''
    for o, a in myopts:
        if o == '-d':
            domain = a
        elif o == '-s':
            status = a
        elif o == '-a':
            action = a
        elif o == '-h':
            helptopic = a
        elif o == '-p':
            try:
                parameter = json.loads(a)
            except ValueError:
                parameter = a;

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
        elif status == 'batches':
            monitorBatches(domain)
        elif status == 'muhimbi':
            monitorMuhimbi(domain)
        else:
            print "Type what status you want to see. statuses {all | dpx | ref | notification | cas | jms | smartprocure | elasticsearch | tax | batches }"
    elif action != '':
        if action == 'dpxnotificationbatch':
            actionDpxNotificationBatch(domain, parameter)
        if action == 'runbatch':
            runbatch(domain, parameter)
        else:
            print "Type what action to perform. actions : {dpxnotificationbatch | runbatch}"
    elif helptopic != '':
        helpdir = '/apps/code/aageno/scripts/help/'
        if helptopic == 'options':
            files =  glob.glob(helpdir+"*.txt")
            for file in files:
                print os.path.splitext(os.path.basename(file))[0]
        else:
            subprocess.call(['vi', helpdir+helptopic+'.txt'])



    else:
        print "Looks like you need some help. -h helptopics"

    from subprocess import Popen, PIPE
    p1 = Popen(['lsof', '-a', '-p9108', '-i4'], stdout=PIPE)
    p2 = Popen(["grep", "LISTEN"], stdin=p1.stdout, stdout=PIPE)
    print p2.communicate()[0]


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
