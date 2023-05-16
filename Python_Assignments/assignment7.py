# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:23:38 2021

@author: dalia
"""

#Get all main urls on a website and save to a text file
# requests for fetching html of website
import requests
from bs4 import BeautifulSoup
import json
import re

url = 'https://www.futhead.com/squad-building-challenges/squads/343/'

def requestAndExtract(url):
    
    # Make the GET request to a url
    r = requests.get(url)
    # Extract the content
    c = r.content
    # Create a soup object
    soup = BeautifulSoup( c, "html.parser")
    # Extract the relevant information as text
    script = soup.find_all('script')[4].string.strip()
    #type = string
    return script

def makeDict(data):
     
    #make list of urls
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
    #convet list items to strings (to make it useable for json to create a dictionary)
    u2 = json.dumps(urls)
    u3 = str(u2)
    #Add property name
    u4 = '{"Urls": ' + u3 + "}"
    #create dictionary
    dct = json.loads(u4)
    return dct

def saveTxt(dictionary):
    
    #write dictionary to file dict.txt
    f = open("dict.txt","w")
    f.write( str(dictionary) )
    f.close()


def main():
    urlData = requestAndExtract(url)
    urlDict = makeDict(urlData)
    print(urlDict)
    
    saveTxt(urlDict)


main()