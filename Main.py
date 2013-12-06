
import webapp2
from Handlers import ParserPublicidad
from Handlers import ParserEventos
from Handlers import ParserGeneral

app = webapp2.WSGIApplication([('/captura_publicidad',ParserPublicidad.Main_Handler),
  ('/guarda_publicidad', ParserPublicidad.Captura_Handler),
  ('/muestra_publicidad', ParserPublicidad.Parser_Handler),
  ('/borra_publicidad', ParserPublicidad.Delete_Handler),
  ('/img', ParserPublicidad.Image_Handler),
  ('/captura_evento', ParserEventos.Captura_Handler),
  ('/guarda_evento', ParserEventos.Guarda_Handler),
  ('/muestra_evento', ParserEventos.Parser_Handler),
  ('/borra_evento', ParserEventos.Borra_Handler),
  ('/evento', ParserEventos.Evento_Parser_Handler),
  ('/main', ParserGeneral.MainPage_Handler),],debug=True)