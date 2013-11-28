import webapp2
from Lib import Manejador_Publicidad
import datetime
import jinja2
import os
from google.appengine.ext import db

jinja_environ = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname('Templates/')))

template_muestra = jinja_environ.get_template('muestra_format.html')
template_borra = jinja_environ.get_template('borra_format.html')

css_Class_Publicidad = 'Publicidad'
css_Class_Publicidad_Imagen = 'Imagen-Publicidad'

class Main_Handler(webapp2.RequestHandler):

  def get(self):
    archivo_html = open('Templates/captura_publicidad.html', 'r')
    #desplegar contenido en navegador
    self.response.write(archivo_html.read())


class Captura_Handler(webapp2.RequestHandler):

  def post(self):
    empresa = self.request.get('empresa')

    lugar = []
    lugar.append(self.request.get('ciudad'))
    lugar.append(self.request.get('estado'))
    lugar.append(self.request.get('pais'))

    url = self.request.get('url')

    imagen = self.request.get('imagen')




    try:
      year = int(self.request.get('year'))
      month = int(self.request.get('month'))
      day = int(self.request.get('day'))
      year_hoy = int(datetime.datetime.today().year)
      fecha_Vencimiento = datetime.datetime(year, month, day)
    except ValueError:
      self.response.write('Fecha Invalida')
      return False

    if year < year_hoy:
      self.response.write('Fecha Atrasada')
      return False

    Manejador_Publicidad.alta(empresa, url, imagen, lugar, fecha_Vencimiento)

    self.response.write('Captura concretada.')



class Delete_Handler(webapp2.RequestHandler):

  def get(self):
    Manejador_Publicidad.borrar_Todo()
    self.response.write('hola como estas Borrado')


class Image_Handler(webapp2.RequestHandler):

  def get(self):
    publicacion = Manejador_Publicidad.buscar_Por_Id(self.request.get('publicacion_id'))
    self.response.headers['Content-Type'] = 'image/jpeg'
    self.response.write(publicacion.imagen)



class Parser_Handler(webapp2.RequestHandler):

  def get(self):
    todo = Manejador_Publicidad.mostrar_Todo()

    links_html = ''

    for publicacion in todo:
      links_html = links_html+('<a href="{!s}" class="{!s}"><img class="{!s}" alt="{!s}" src="img?publicacion_id={!s}"/></a>'.format(publicacion.url,
      css_Class_Publicidad,
      css_Class_Publicidad_Imagen,
      publicacion.empresa,
      publicacion.key()))

    template_values = {
      'titulo': 'Publicidad',
      'links': links_html,
      }

    self.response.write(template_muestra.render(template_values))
    ##self.response.write(links_html)