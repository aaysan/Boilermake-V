from foodapi_Clarifai import fooditem
import pymongo
from pymongo import MongoClient
import datetime
import pprint


cluster = MongoClient('mongodb://maysan:Horizon96*@boilermakev-shard-00-00-uhw0t.mongodb.net:27017,\
boilermakev-shard-00-01-uhw0t.mongodb.net:27017,boilermakev-shard-00-02-uhw0t.mongodb.\
net:27017/inventory?ssl=true&replicaSet=BoilermakeV-shard-0&authSource=admin')

pprint.pprint(cluster)

db = cluster.inventory ##database
pprint.pprint(db)
foodinventory = db.food ##collection
pprint.pprint(foodinventory)


food = fooditem('oranges.jpg'); #select food[0] as correct for now

post = None
item = foodinventory.find_one({"food":food})
pprint.pprint(item)


if(item == None):
    newitem = {"food": food[0],
            "amount": 1,
            "dateAdded": datetime.datetime.utcnow(),
            "PossibleExpiry": None}
    foodinventory.insert_one(newitem)
else:
    foodinventory.updateOne({"food":food}, { inc: {quantity: 10}})

##find the amount in item and add 1 to it.
