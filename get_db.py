import pymongo
from pymongo import MongoClient
import datetime
import pprint

def get_db():
	cluster = MongoClient('mongodb://maysan:Horizon96*@boilermakev-shard-00-00-uhw0t.mongodb.net:27017,\
	boilermakev-shard-00-01-uhw0t.mongodb.net:27017,boilermakev-shard-00-02-uhw0t.mongodb.\
	net:27017/inventory?ssl=true&replicaSet=BoilermakeV-shard-0&authSource=admin')

	db = cluster.inventory
	foodinventory = db.foods
	jlist = list(foodinventory.find())
	food = []
	amt = []
	expire = []
	for dic in jlist:
		if (dic['amount'] <= 0): continue
		sorted(dic['PossibleExpiry'])
		food.append(dic['food'])
		amt.append(dic['amount'])
		expire.append(dic['PossibleExpiry'][0]['Date'].strftime("%m/%d/%y"))
	return food, amt, expire

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
