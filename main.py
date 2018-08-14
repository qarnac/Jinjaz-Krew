import webapp2
import jinja2
import os
import logging

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FoodType(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('GetFoodType')
        mypage = env.get_template('templates/homepage.html')
        self.response.write(mypage.render())
    def post(self):
        logging.info('PostFoodType')
        mypage = env.get_template('templates/homepage.html')
        self.response.write(mypage.render())

class FoodInfo(webapp2.RequestHandler):
    def get(self):
        logging.info('GetFoodInfo')
        mypage = env.get_template('templates/randomfood.html')
        self.response.write(mypage.render())

    def post(self):
        logging.info('PostFoodInfo')
        mypage = env.get_template('templates/randomfood.html')
        self.response.write(mypage.render())

app = webapp2.WSGIApplication([
    ('/', FoodType),
    ('/random',FoodInfo )
    #('/', )
], debug=True)
