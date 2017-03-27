import fire
import configparser
import subprocess
import os
import urllib2
import urllib2
import bs4
import json
import sys
import glob
import os



class Kanchi(object):

  def runAndPrintCommand(self,command):
      action = subprocess.Popen(command, stdout=subprocess.PIPE)
      output = action.communicate()[0]
      print output

  def getSysConfig(self,section, key):
      config = configparser.ConfigParser()
      config.read('/etc/aageno/data.ini')
      return config[section][key]

  def notebackup(self):
      os.chdir(self.getSysConfig('aageno_app', 'aagenoBase') + '/notes/')
      self.runAndPrintCommand(['./brahman.py'])

  def camerafix(self):
      print "sudo killall VDCAssistant";
      self.runAndPrintCommand(['sudo','killall','VDCAssistant'])

  def help(self):
      print "camerafix | note | notebackup"

  def log(self,title,story):
      from elasticsearch import TransportError
      from elasticsearch import Elasticsearch

      note = {}
      note["maintag"] = title
      note["body"] = story

      es = Elasticsearch([self.getSysConfig('aageno_app', 'elasticSearchUrl')])
      if len(title) > 0:
         print "Indexing with title "+title
         try:
            es.index(index="brahman", doc_type='note', id=title, body=note)
         except TransportError as e:
            print(e.info)
      else:
         print "Indexing with title : "+title
         es.index(index="brahman", doc_type='note', body=note)

      print "Your story has been saved"



  def note(self, helptopic):
      helpdir = self.getSysConfig('aageno_app', 'aagenoBase') + '/scripts/help/'
      if helptopic == 'options' or helptopic == '':
          files = glob.glob(helpdir + "*.txt")
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

if __name__ == '__main__':
  fire.Fire(Kanchi)
