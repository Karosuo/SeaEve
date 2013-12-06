import webapp2
from Lib import Manejador_Eventos
import datetime
import jinja2
import os


jinja_environ = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname('Templates/')))


template_captura = jinja_environ.get_template('captura_evento_format.html')


div_CSS_Class_Gratuito = 'Gratuito'
icon_CSS_Class = 'icono'
url_evento = '/evento'
link_CSS_Class = 'link_evento'
img_CSS_Class = 'imagen_link_evento'
footer_Img_CSS_Class = 'footer_Img'


class Guarda_Handler(webapp2.RequestHandler):

	def post(self):
		nombre = self.request.get('nombre');
		imagen = self.request.get('imagen')
		descripcion = self.request.get('descripcion')

		#FALTA VALIDAR URLS CORRECTAS PARA SU CAPTURA.
		#Un modulo con regexes, aprox "isURL(string url):boolean"
		contacto = [];
		if self.request.get('facebook'):
			contacto.append("facebook")
			url_facebook = self.request.get('url_Facebook')
			contacto.append("url_Facebook")

		if self.request.get('twitter'):
			contacto.append('twitter')
			url_twitter = self.request.get('url_Twitter')
			contacto.append('url_Twitter')

		if self.request.get('googlep'):
			contacto.append('googlep')
			url_googlep = self.request.get('url_Googlep')
			contacto.append('url_Googlep')


		tags = self.request.get('tags').split()


		year = float(self.request.get('year'))
		month = float(self.request.get('month'))
		day = float(self.request.get('day'))

		fecha_realizacion = datetime.datetime(int(year), int(month), int(day))

		if self.request.get('tipo'):
			evento_Pagado = true;

		coordenadas[0] = self.request.get('coordX')
		coordenadas[1] = self.request.get('coordY')

		costo = self.request.get('costo')

		categoria = self.request.get('categoria')

		if self.request.get('estado'):
			estado = true

		direccion = self.request.get('direccion')

		edad = self.request.get('edad')

		self.response.write("Guardado exitosamente.")


class Borra_Handler(webapp2.RequestHandler):

	def get(self):
		html = '''<form action="/borra_evento" method="post">
					<div><input type="submit" value="Borrar Base de datos">
					</div> </form>'''
		self.response.write(html)

	def post(self):
		Manejador_Eventos.borrar_Todo()
		self.response.write('Base de datos borrada.')

	

class Parser_Handler(webapp2.RequestHandler):

	def get(self):
		todos_Eventos = Manejador_Eventos.mostrar_Todo()

		contenedor_Html = ""

		for evento in todos_Eventos:
			contenedor_Html = contenedor_Html + '''<div class="{!s}">
												<!--Anchor con imagen principal para darle click y desplegar m[as info en /evento-->
												<a href="{!s}" class="{!s}"><img class="{!s}" alt="{!s}" src="img?publicacion_id={!s}"/><div class="{!s}">
												<!--Div con imagen de footer de evento mini principal--></div>
												</div>'''.format(div_CSS_Class_Gratuito,
													url_evento,
													link_CSS_Class,
													img_CSS_Class,
													evento.nombre,
													evento.key(),
													footer_Img_CSS_Class)


class Captura_Handler(webapp2.RequestHandler):

	def get(self):
		archivo_Captura_Html = open('Templates/captura_evento.html','r')
		option_html_tag = '<option value="{!s}">{!s}</option>'
		
		days_html = ''
		months_html = ''
		years_html = ''
		edad_html=''

		year = datetime.timedelta(days=365)

		for contador in xrange(1,32):
			
			if contador <= 12:
				months_html = months_html + option_html_tag.format(contador, contador)
			
			if contador <= 5:
				years_html = years_html + option_html_tag.format(datetime.date.today().year + contador-1, datetime.date.today().year + contador-1)				
				#years_html = years_html + option_html_tag.format(str(actual_Year+change), str(actual_Year+change))
			
			days_html = days_html + option_html_tag.format(contador, contador)

		for edad in xrange(15,45):
			edad_html = edad_html + option_html_tag.format(edad, edad)



		template_values = {
			'days': days_html,
			'months': months_html,
			'years': years_html,
			'edad': edad_html,
		}

		self.response.write(template_captura.render(template_values))
		


class Evento_Parser_Handler(webapp2.RequestHandler):

	def get(self):		
		self.response.write("Evento descripcion completa")

