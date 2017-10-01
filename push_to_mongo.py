from foodapi_Clarifai import fooditem
import pymongo
from pymongo import MongoClient
import datetime
import pprint
cluster = MongoClient('mongodb://maysan:Horizon96*@boilermakev-shard-00-00-uhw0t.mongodb.net:27017,\
boilermakev-shard-00-01-uhw0t.mongodb.net:27017,boilermakev-shard-00-02-uhw0t.mongodb.\
net:27017/inventory?ssl=true&replicaSet=BoilermakeV-shard-0&authSource=admin')
def push_to_mongo(foodstr, amounttoadd, possibexp):
    db = cluster.inventory ##database
    foodinventory = db.foods ##collection
    amount = amounttoadd #this will come in
    possibleExpiry = possibexp #this will come in


    food = foodstr; #this will come in
    item = foodinventory.find_one({"food":food})


    if(item == None):
        newitem = {"food": food,
                "amount": amount,
                "dateAdded": datetime.datetime.utcnow(),
                "PossibleExpiry": [{"Date": possibleExpiry,
                                    "amt":  amount
                }]}
        foodinventory.insert_one(newitem)
    else:
        foodinventory.update_one({'food':food}, { '$inc': {'amount': amount}})
        foodinventory.update({'food':food},
                                { '$push': {'PossibleExpiry':{"Date": possibleExpiry,"amt":  amount}}})
