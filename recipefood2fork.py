import urllib2
import urllib
import json
from functools import partial
import pprint


class food2fork(): #food2fork api call class
  
    def __init__(self,debug=True):
        self.apiKey = '659e07599169d079170d7db52af74c0d'
        self.debugMode = debug
        self.SEARCH_ENDPOINT = 'http://food2fork.com/api/search'
        self.VIEW_ENDPOINT   = 'http://food2fork.com/api/get'
        self.MAX_PAGESIZE = 30

    def search(self,query):
        self.url =  "http://food2fork.com/api/search?key="+self.apiKey+"&q="
        l = query.strip().split()
        for i in range(len(l)-1):
            self.url += l[i]+"%20"
        self.url += l[-1]
        print self.url
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} #header info so request is not banned
        req = urllib2.Request(self.url,None,headers=hdr)
        f = urllib2.urlopen(req)
        data = json.loads(f.read())
        return data

    def get(self,id1):
        self.url =  "http://food2fork.com/api/get?key="+self.apiKey+"&rId="+id1
       
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} #header info so request is not banned
        req = urllib2.Request(self.url,None,headers=hdr)
        f = urllib2.urlopen(req)
        data = json.loads(f.read())
        return data
        

    
f2f = food2fork()
sr = f2f.search("Chicken biryani") #search results
#pprint.pprint(sr)
gr = f2f.get(sr['recipes'][0]['recipe_id']) #get results
ingredients = gr['recipe']['ingredients']
print ingredients

