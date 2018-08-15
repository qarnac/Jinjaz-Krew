import webapp2
import jinja2
import os
import logging
from models import getUrl

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
      autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/homepage.html')
        self.response.write(mypage.render())
    def post(self):
        foodName = self.request.get('foodName')
        restriction = self.request.POST.getall('restrictions')
        json_object = getUrl(foodName,restriction)

        #mypage = env.get_template('templates/randomfood.html')
        self.response.write(json_object)
class RandomPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/randomfood.html')
        self.response.write(mypage.render())
    #def post(self):

class AboutPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/aboutus.html')
        self.response.write(mypage.render())
    #def post(self):


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/random', RandomPage),
    ('/about', AboutPage)
], debug=True)
