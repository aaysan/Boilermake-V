#need to install clarify (pip)
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import pprint
app = ClarifaiApp(api_key='e5af645934f34cee8ec140028c1fff12')

def fooditem(new_image):
    model = app.models.get('food-items-v1.0')
    image = ClImage(file_obj=open(new_image, 'rb'))
    r =  model.predict([image])
    food_items = dict()
    #pprint.pprint(model.predict([image]))
    food_items = [r['outputs'][0]['data']['concepts'][0]['name'], \
                 r['outputs'][0]['data']['concepts'][1]['name'], \
                 r['outputs'][0]['data']['concepts'][2]['name'], \
                 r['outputs'][0]['data']['concepts'][3]['name'], \
                 r['outputs'][0]['data']['concepts'][4]['name']]
    return food_items
    #print r['outputs'][0]['data']['concepts'][0]['name'] #Option 1
    #print r['outputs'][0]['data']['concepts'][1]['name'] #Option 2
    #print r['outputs'][0]['data']['concepts'][2]['name'] #Option 3
    #print r['outputs'][0]['data']['concepts'][3]['name'] #Option 4
    #print r['outputs'][0]['data']['concepts'][4]['name'] #Option 5
