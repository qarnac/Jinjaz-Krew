import urllib2
import json

def getUrl(foodName, restrictionsList, caloriesMin, caloriesMax, healthInfo):
    food_name = foodName
    restrictions = restrictionsList
    maxCalories = caloriesMax
    minCalories = caloriesMin
    health_restrictions = healthInfo

    params =[(
        ('api_key' , 'b4dc98f7d320f1968ef7b63205e2e462'),
        ('app_id' , '28c73d69'),
        ('q' , food_name),
        ('calories' , minCalories + '-' + maxCalories)
    )]
    for restrictions in health_restrictions:
        params.insert(0, ('health', restrictions))
    for restrictions in restrictions:
        params.insert(0, ('excluded', restrictions))
    form_data = urllib.urlencode(params)
    api_url = 'https://api.edamam.com/search?' + form_data

    request = urllib2.Request(api_url)
    response = urllib2.urlopen(request).read()
    content = json.loads(response)

    return content
