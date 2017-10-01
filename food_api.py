import requests
from PIL import Image
import pprint


def fooditem(new_image):
	img = Image.open(new_image)
	img = img.resize((544,544))
	save = 'tmp.jpeg'
	img.save(save, "JPEG")
	headers = {
	    'Content-Type': 'image/jpeg',
	}

	params = (
	    ('user_key', 'bef7083a603ab9155793a863d466d6c7'),
	    #('user_key', 'ddc40232c609f21b0c45e0bc81c23125'), # real
	    
	)

	data = open(save, 'rb').read()
	r = requests.post('https://api-2445582032290.production.gw.apicast.io/v1/foodrecognition', headers=headers, params=params, data=data)
	m = r.json()
	#NB. Original query string below. It seems impossible to parse and
	#reproduce query strings 100% accurately so the one below is given
	#in case the reproduced version is not "correct".
	# requests.post('https://api-2445582032290.production.gw.apicast.io/v1/foodrecognition?user_key=YOUR', headers=headers, data=data)
	n = len(m)
	count = 0
	final = []
	if 'results' not in m: return []
	for i in m['results']:
	    if count>4:
	        break
	    final += [i['group']]
	    count += 1

	return final
