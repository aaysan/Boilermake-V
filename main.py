from flask import Flask
import camera
import barcode

# pip install Flask

# export FLASK_APP=hello.py
# flask run

app = Flask(__name__)

@app.route('/barcode')
def barcode():
	camera.main()
	return barcode.main()
    