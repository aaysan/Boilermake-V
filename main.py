from flask import Flask
import camera
import recipefood2fork as recipe_api
import barcode
import foodapi_Clarifai as clarifai_api
import food_api as food_api

# pip install Flask

# export FLASK_APP=main.py
# flask run

app = Flask(__name__)

@app.route('/')
def barcode():
	return "hello world"

# @app.route('/barcode')
# def barcode():
# 	camera.capture()

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
		candidates.append("")
	return str(candidates)

@app.route('/recipe/<recipe>')
def getrecipes(recipe):
	# get recipe name from alp database
	print(recipe)
	fridge = ['chicken', 'butter', 'water', 'rice']
	output = recipe_api.get_recipe(recipe)[0]
	missing = []
	for ingredient in output:
		found = False
		for has in fridge:
			if has in ingredient:
				found = True
		if not found:
			missing.append(ingredient)
	return str(missing)



if __name__=='__main__':
    app.run(host='0.0.0.0')