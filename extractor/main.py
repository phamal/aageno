#!/usr/bin/python
import urllib2
import bs4
import json
import sys
from elasticsearch import  Elasticsearch
sys.path.append('entities/')


links = {}
companies = [{}]

def indexCompany(company):
    es = Elasticsearch(['http://159.203.66.191:9200'])
    res = es.index(index="nepalstock", doc_type='company', id=company["symbol"], body=company)
    print(res['created'])


def scrapCompanyDetail(company):
    print company["detaillink"]
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(company["detaillink"])
    soup = bs4.BeautifulSoup(page, "lxml")
    trs = soup.select("#company-view table.my-table tr")
    for tr in trs:
        tds = tr.select("td")
        if len(tds) > 1:
            key = tds[0].getText().strip()
            value = tds[1].getText().strip()
            print key+" : "+value



def scrapCompanies(url):
    print "Scrapping contents from : "+url
    links[url] = True

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(url)
    soup = bs4.BeautifulSoup(page,"lxml")
    trs = soup.select("#company-list table.my-table tr")

    for tr in trs:
        tds = tr.select("td")
        if len(tds) > 4:
            company = {}
            company["name"] = tds[2].getText().strip()
            company["symbol"] = tds[3].getText().strip()
            company["sector"] = tds[4].getText().strip()
            company["detaillink"] = ""
            linkTD = tds[5]
            companyLinks = linkTD.select("a")
            if len(companyLinks) > 0:
                detailLink = companyLinks[0].attrs["href"]
                company["detaillink"] = detailLink
                scrapCompanyDetail(company)

            indexCompany(company)


    allLinks = soup.select("a")

    for link in allLinks:
        if 'title' in link.attrs:
            title = link.attrs["title"];
            if title.find("Go to Page") != -1 or title.find("Next Page") != -1 or title.find("Last Page") != -1:
                url = link.attrs["href"].strip()
                if url not in links:
                    links[url] = False


    nextUrl = ''
    for link in links:
        if links[link] == False:
            nextUrl = link


    if nextUrl != '':
        scrapCompanies(nextUrl)


def main():

    url = 'http://www.nepalstock.com/company'
    scrapCompanies(url)
    print "Total companies found : "+str(len(companies))
    for company in companies:
        if 'symbol' in company:
            print company["symbol"]+" : "+company["name"]


main()
