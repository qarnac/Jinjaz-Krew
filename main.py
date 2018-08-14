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
        json = getUrl(self.request.get('typeOfFood'),
                self.request.get('restrictions', allow_multiples = True),
                )
        mypage = env.get_template('templates/randomfood.html')
        self.response.write(mypage.render())


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
