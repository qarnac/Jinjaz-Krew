import webapp2
import jinja2
import os
import logging

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/homepage.html')
        self.response.write(mypage.render())
    def post(self):
        mypage = env.get_template('templates/homepage.html')
        self.response.write(mypage.render())

class RandomFood(webapp2.RequestHandler):
    def get(self):  # for a get request
        mypage = env.get_template('templates/randomfood.html')
        self.response.write(mypage.render())
    def post(self):
        mypage = env.get_template('templates/homepage.html')
        self.response.write(mypage.render())

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
