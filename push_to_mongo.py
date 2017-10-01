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
    todaysdate = datetime.datetime.utcnow()
    expirydate = todaysdate + datetime.timedelta(days=possibexp)

    if(item == None):
        newitem = {"food": food,
                "amount": amount,
                "dateAdded": todaysdate,
                "PossibleExpiry": [{"Date": expirydate,
                                    "amt":  amount
                }]}
        foodinventory.insert_one(newitem)
    else:
        foodinventory.update_one({'food':food}, { '$inc': {'amount': amount}})
        flag = 0
        items = list(foodinventory.find({'food':food}))
        print(items)
        for item in items:
            if (item is None or len(item['PossibleExpiry']) == 0 or item['PossibleExpiry'][0] is None):
                break
            print( item['PossibleExpiry'][0]['Date'])
            print (expirydate)
            if item['PossibleExpiry'][0]['Date'].date() == expirydate.date():
                item['PossibleExpiry'][0]['amt'] += amount
                foodinventory.update_one({'food':food}, {'$set':{ 'PossibleExpiry': item['PossibleExpiry']}})
                #item['PossibleExpiry'][0]['amt'] += amount
                flag = 1
                break

        if flag != 1:
            foodinventory.update({'food':food},
                                { '$push': {'PossibleExpiry':{"Date": expirydate,"amt":  amount}}})
