import webapp2
import jinja2
import os
import logging
from models import getUrl
import json
import urllib2
from google.appengine.api import *

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
      autoescape=True)

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
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                json_object = json.loads(result.content)
                logging.info(json_object['hits']['recipe'])

                mypage = env.get_template('templates/randomfood.html')
                self.response.write(json_object)
            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
        #
class RandomPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/randomfood.html')
        self.response.write(mypage.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/aboutus.html')
        self.response.write(mypage.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/random', RandomPage),
    ('/about', AboutPage)
], debug=True)
