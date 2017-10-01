from flask import Flask, request
import camera
import recipefood2fork as recipe_api
import barcode
import foodapi_Clarifai as clarifai_api
import food_api as food_api
import push_to_mongo as add
import pull_from_mongo as remove
import get_db

# pip install Flask

# export FLASK_APP=main.py
# flask run

app = Flask(__name__)

@app.route('/')
def barcode():
	return "hello world"

@app.route('/add/<string1>')
def addfood(string1):
	print(string1)
	foodstr, amtadd, exp = string1.split(' ')
	add.push_to_mongo(foodstr, int(amtadd), int(exp))
	return foodstr + " " + amtadd + " " + exp


@app.route('/remove/<string1>')
def removefood(string1):
	print(string1)
	foodstr, amtadd = string1.split(' ')
	remove.pull_from_mongo(foodstr, int(amtadd))
	return foodstr + " " + amtadd

# @app.route('/barcode')
# def barcode():
# 	camera.capture()

@app.route('/get_pantry/')
def get_pantry():
	food, amt, expire = get_db.get_db()
	string = ''
	for i in range(len(food)):
		string += food[i] + " " + str(amt[i]) + " " + str(expire[i]) + ";"
	return string


@app.route('/object/')
def object():
	camera.capture()
	candidates = clarifai_api.fooditem("pic1.jpeg")
	for candidate in food_api.fooditem("pic1.jpeg"):
		candidate = candidate.lower()
		if candidate in candidates:
			continue
		candidates.append(candidate)
	while len(candidates) < 10:
		candidates.append(" ")
	return ";".join(candidates)

@app.route('/recipe/<recipe>')
def getrecipes(recipe):
	# get recipe name from alp database
	fridge, amt, expire = get_db.get_db()
	output, title = recipe_api.get_recipe(recipe)
	output, title = output[0], title[0]
	missing = []
	for ingredient in output:
		found = False
		for has in fridge:
			if has.lower() in ingredient.lower():
				found = True
		if not found:
			missing.append(ingredient)
	return title + ":" + ";".join(missing)



if __name__=='__main__':
    app.run(host='0.0.0.0')