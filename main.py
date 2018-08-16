import webapp2
import jinja2
import os
import logging
from models import getUrl
import json
import urllib2
from random import randint
from google.appengine.api import *

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
      autoescape=True)

class TitlePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/title.html')
        self.response.write(mypage.render())

class MainPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/select.html')
        self.response.write(mypage.render())
    def post(self):
        foodName = self.request.get('foodName')
        restriction = self.request.POST.getall('restrictions')
        health = self.request.POST.getall('health')
        url = getUrl(foodName,restriction,health)

        try:
            result = urllib2.urlopen(url).read()
            json_object = json.loads(result)
            mypage = env.get_template('templates/randomfood.html')
            rand = randint(0,len(json_object))
            food_name = json_object['hits'][rand]['recipe']['label']
            totalTime = json_object['hits'][rand]['recipe']['totalTime']
            imageFile = json_object['hits'][rand]['recipe']['image']
            linkUrl = json_object['hits'][rand]['recipe']['url']
            cal = json_object['hits'][rand]['recipe']['calories']
            cal = int(cal)
            ingr = ''
            ingredients = json_object['hits'][rand]['recipe']['ingredientLines']
            for items in ingredients:
                ingr += items + ', '
            self.response.write(mypage.render({'foodName' : food_name, 'time' : totalTime, 'img' : imageFile, 'link' : linkUrl,
                                                'calories' : cal, 'ingredients' : ingr}))
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

class AboutPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/aboutcrave.html')
        self.response.write(mypage.render())

app = webapp2.WSGIApplication([
    ('/', TitlePage),
    ('/select', MainPage),
    ('/about', AboutPage),
], debug=True)
