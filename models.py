def getUrl(foodName, restrictionsList, caloriesCounter, healthInfo):
    food_name = foodName
    restrictions = restrictionsList
    calories = caloriesCounter
    health_restrictions = healthInfo
    search_term ={
        api_key : 'b4dc98f7d320f1968ef7b63205e2e462',
        app_id : '28c73d69',
        q : food_name

    }

    url = 'https://api.edamam.com/search?' + app_id  + '&' + app_key
