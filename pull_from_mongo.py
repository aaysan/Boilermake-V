import pymongo
from pymongo import MongoClient
import datetime
import pprint

def pull_from_mongo(removedfood, removedamount):
	cluster = MongoClient('mongodb://maysan:Horizon96*@boilermakev-shard-00-00-uhw0t.mongodb.net:27017,\
	boilermakev-shard-00-01-uhw0t.mongodb.net:27017,boilermakev-shard-00-02-uhw0t.mongodb.\
	net:27017/inventory?ssl=true&replicaSet=BoilermakeV-shard-0&authSource=admin')

	db = cluster.inventory
	foodinventory = db.foods
	food_to_remove = removedfood
	amount_to_remove = removedamount

	item = foodinventory.find_one({"food":food_to_remove})
	pprint.pprint(item)

	if(item == None):
		return
	amount_to_remove = amount_to_remove * -1
	foodinventory.update_one({'food':food_to_remove},{ '$inc': {'amount': amount_to_remove}})

	currentamount = foodinventory.find_one({'food':food_to_remove},{'amount':1})
	print currentamount['amount']
	if(currentamount['amount'] <= 0):
	    foodinventory.update_one({'food':food_to_remove}, { '$set': {'amount': 0}})
	    foodinventory.update_one({'food':food_to_remove}, { '$set': {'PossibleExpiry':[]}})
	    return

	# items = foodinventory.find({'food':food_to_remove})
	#
	# for item in items:
	# 	i = len(item['PossibleExpiry']) - 1
	# 	item['PossibleExpiry'] = sorted(item['PossibleExpiry'], reverse = True)
	# 	amount_present = item['PossibleExpiry'][i]['amt']
	#
	# 	while amount_to_remove > 0:
	#
	# 		if(amount_to_remove > amount_present):
	# 			amount_to_remove -= amount_present
	# 			item[PossibleExpiry][i].remove()
	# 		else:
	# 			amount_to_remove = 0;
	# 			item[PossibleExpiry][i]['amt'] -= amount_to_remove
			# 
			# foodinventory.update_one({'food':food}, {'$set':{ ' PossibleExpiry': item[PossibleExpiry]}})
			# i-= 1
