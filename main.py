import webapp2
import jinja2
import os
import logging
from models import *

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
      autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/homepage.html')
        self.response.write(mypage.render())
    def post(self):
        #json_object = getUrl(self.request.get('foodName'),
            #    self.request.get('restrictions', allow_multiples = True),
            #    self.request.get('minCal'),
            #    self.request.get('maxCal'),
            #    self.request.get('health', allow_multiples = True))

        #logging.info(str(json_object))
        mypage = env.get_template('templates/randomfood.html')
        self.response.write(mypage.render())


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
