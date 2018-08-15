import urllib2
import json
from google.appengine.api import *

def getUrl(foodName,restrictionsList):
    # restrictionsList, caloriesMin, caloriesMax, healthInfo
    food_name = 'q=' + foodName
    restrictions = ""
    for item in restrictionsList:
        restrictions += '&exclude=' + item
    #maxCalories = caloriesMax
    #minCalories = caloriesMin
#    health_restrictions = healthInfo

    url = 'https://api.edamam.com/search?app_id=28c73d69&app_key=b4dc98f7d320f1968ef7b63205e2e462&' + food_name + restrictions
    try:
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            data = result.content
            return data
        else:
            self.response.status_code = result.status_code
    except urlfetch.Error:
        logging.exception('Caught exception fetching url')
