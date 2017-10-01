import pymongo
from pymongo import MongoClient
import datetime
import pprint

cluster = MongoClient('mongodb://maysan:Horizon96*@boilermakev-shard-00-00-uhw0t.mongodb.net:27017,\
boilermakev-shard-00-01-uhw0t.mongodb.net:27017,boilermakev-shard-00-02-uhw0t.mongodb.\
net:27017/inventory?ssl=true&replicaSet=BoilermakeV-shard-0&authSource=admin')

db = cluster.inventory
foodinventory = db.foods
food_to_remove = "juice"
amount_to_remove = 3;

item = foodinventory.find_one({"food":food_to_remove})
pprint.pprint(item)

if(item == None):
    quit()

amount_to_remove = amount_to_remove * -1
foodinventory.update_one({'food':food_to_remove},{ '$inc': {'amount': amount_to_remove}})

currentamount = foodinventory.find_one({'food':food_to_remove},{'amount':1})
print currentamount['amount']
if(currentamount['amount'] <= 0):
    foodinventory.update_one({'food':food_to_remove}, { '$set': {'amount': 0}})
    foodinventory.update_one({'food':food_to_remove}, { '$set': {'PossibleExpiry':[]}})
    quit()

expirydates = foodinventory.find({'food':food_to_remove},{'PossibleExpiry':1})
pprint.pprint(expirydates)
