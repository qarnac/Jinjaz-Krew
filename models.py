import urllib2
import json
import logging


def getUrl(foodName,restrictionsList,healthList):
    # restrictionsList, caloriesMin, caloriesMax, healthInfo
    food_name = 'q=' + foodName
    restrictions = ""
    health = ''
    for items in healthList:
        health += '&health=' + items
    for item in restrictionsList:
        restrictions += '&exclude=' + item
        
    logging.info('health' + health)
    #maxCalories = caloriesMax
    #minCalories = caloriesMin
#    health_restrictions = healthInfo

    url = 'https://api.edamam.com/search?app_id=28c73d69&app_key=b4dc98f7d320f1968ef7b63205e2e462&' + food_name + restrictions + health
    return url
