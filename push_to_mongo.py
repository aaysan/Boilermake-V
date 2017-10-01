from foodapi_Clarifai import fooditem
import pymongo
from pymongo import MongoClient
import datetime
import pprint

def push_to_mongo(foodimg, amounttoadd, possibexp):
    cluster = MongoClient('mongodb://maysan:Horizon96*@boilermakev-shard-00-00-uhw0t.mongodb.net:27017,\
    boilermakev-shard-00-01-uhw0t.mongodb.net:27017,boilermakev-shard-00-02-uhw0t.mongodb.\
    net:27017/inventory?ssl=true&replicaSet=BoilermakeV-shard-0&authSource=admin')

    db = cluster.inventory ##database
    foodinventory = db.foods ##collection
    amount = amounttoadd #this will come in
    possibleExpiry = possibexp #this will come in


    food = fooditem(foodimg); #this will come in
    item = foodinventory.find_one({"food":food[0]})


    if(item == None):
        newitem = {"food": food[0],
                "amount": amount,
                "dateAdded": datetime.datetime.utcnow(),
                "PossibleExpiry": [{"Date": possibleExpiry,
                                    "amt":  amount
                }]}
        foodinventory.insert_one(newitem)
    else:
        foodinventory.update_one({'food':food[0]}, { '$inc': {'amount': amount}})
        foodinventory.update({'food':food[0]},
                                { '$push': {'PossibleExpiry':{"Date": possibleExpiry,"amt":  amount}}})
