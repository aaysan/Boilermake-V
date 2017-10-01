#import urllib2
import requests as r
import json
from functools import partial
import pprint


class food2fork(): #food2fork api call class
  
    def __init__(self,debug=True):
        self.apiKey = '2c77b139277a69749964b3f865acba70'
       

    def search(self,query):
        url =  "http://food2fork.com/api/search?key="+self.apiKey+"&q="
        l = query.strip().split()
        for i in range(len(l)-1):
            url += l[i]+"%20"
        url += l[-1]
        #print url
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} #header info so request is not banned
        # req = urllib2.Request(url,None,headers=hdr)
        # f = urllib2.urlopen(req)
        req = r.put(url,data=hdr)
        data = json.loads(req.text)
        return data

    def get(self,id1):
        url =  "http://food2fork.com/api/get?key="+self.apiKey+"&rId="+id1
       
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} #header info so request is not banned
        req = r.put(url,data=hdr)
        data = json.loads(req.text)
        return data
        

def get_recipe(item):
    ingredients = []
    recipes = []
    f2f = food2fork()
    sr = f2f.search(item) #search results
    #pprint.pprint(sr)
    for i in range(5):
      try:
          gr = f2f.get(sr['recipes'][i]['recipe_id'])#get results
          #pprint.pprint(gr)
          ingredients += [gr['recipe']['ingredients']]
          recipes.append(gr['recipe']['title'])
      except:
          break
    return ingredients, recipes

# pprint.pprint(get_recipe("pad thai"))
