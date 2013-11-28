
import webapp2
from Handlers import Parser


app = webapp2.WSGIApplication([('/captura_publicidad',Parser.Main_Handler),
  ('/guarda_publicidad', Parser.Captura_Handler),
  ('/muestra_publicidad', Parser.Parser_Handler),
  ('/borra_publicidad', Parser.Delete_Handler),
  ('/img', Parser.Image_Handler),],debug=True)