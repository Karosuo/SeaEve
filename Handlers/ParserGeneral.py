import webapp2
import datetime
import jinja2
import os

jinja_environ = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname('Templates/')))

template_muestra = jinja_environ.get_template('muestra_format.html')
template_borra = jinja_environ.get_template('borra_format.html')



class MainPage_Handler(webapp2.RequestHandler):

	def get(self):
		self.response.write("Parser principal")