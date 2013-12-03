
import webapp2
from Handlers import ParserPublicidad
from Handlers import ParserEventos

app = webapp2.WSGIApplication([('/captura_publicidad',ParserPublicidad.Main_Handler),
  ('/guarda_publicidad', ParserPublicidad.Captura_Handler),
  ('/muestra_publicidad', ParserPublicidad.Parser_Handler),
  ('/borra_publicidad', ParserPublicidad.Delete_Handler),
  ('/img', ParserPublicidad.Image_Handler),
  ('/captura_evento', ParserEventos.Captura_Handler),
  ('/muestra_evento', ParserEventos.Parser_Handler),
  ('/main', ParserGeneral.Main),],debug=True)