from pyzbar.pyzbar import decode
from urllib.parse import urlparse
from PIL import Image
from pprint import *
import requests as r
# import the necessary packages
import numpy as np
import cv2

# pip install pyzbar
# pip install pyzbar[scripts]

BARCODE_API = 'https://api.upcitemdb.com/prod/trial/lookup?upc='

def getBarcode(imagepath):
	# input image path
	# output string of barcode
	h = decode(Image.open('barcode_01.jpg'))
	if (len(h) < 1): return None
	return h[0].data.decode('utf-8')

def getTitle(barcode):
	url = BARCODE_API + barcode
	resp = r.get(url)
	tmp = resp.json()
	return tmp['items'][0]['title']


def main():
	barcode = getBarcode('barcode_01.jpg')
	if barcode is None: return "barcode not found"
	return getTitle(barcode)
