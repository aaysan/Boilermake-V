from pyzbar.pyzbar import decode
from urllib.parse import urlparse
from PIL import Image
from pprint import *
import requests as r

BARCODE_API = 'https://api.upcitemdb.com/prod/trial/lookup?upc='

def getBarcode(imagepath):
	# input image path
	# output string of barcode
	h = decode(Image.open('barcode_01.jpg'))
	return h[0].data.decode('utf-8')

def getTitle(barcode):
	url = BARCODE_API + barcode
	resp = r.get(url)
	tmp = resp.json()
	return tmp['items'][0]['title']


if __name__ == '__main__':
	barcode = getBarcode('barcode_01.jpg')
	print(getTitle(barcode))