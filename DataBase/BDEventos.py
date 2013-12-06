import datetime
from google.appengine.ext import db


class Eventos(db.Model):
    nombre=db.StringProperty()
    imagen = db.BlobProperty() #Imagen del banner
    descripcion = db.StringProperty(multiline=True) #Descripcion
    contacto = db.StringListProperty()
    tags = db.StringListProperty()
    evento_Pagado = db.BooleanProperty()#true, false
    fecha_Evento = db.DateTimeProperty()#cuando se realizara al evento
    fecha_Registro = db.DateTimeProperty(auto_now_add=True)#cuando lo publico
    coordenadas_Mapa = db.GeoPtProperty()#coordenadas del mapa
    costo = db.FloatProperty() #costo del evento
    categoria = db.StringProperty()#categoria del evento, solo una
    estado = db.BooleanProperty()#activo o inactivo (no realizado o realizado)
    direccion = db.StringProperty(multiline=True)
    organizador = db.UserProperty()
    rango_Edad = db.StringProperty()


    def set_CoordenadasMapa(self, coordList):
        coordenadas_Mapa = db.GeoPt(coordList[0], coordList[1])


    def set_Image(self, nueva_Imagen):
        self.imagen = db.Blob(nueva_Imagen)

    def All(self):
        query_str = "SELECT * FROM Eventos"
        return db.GqlQuery(query_str)

    def DeleteAll(self):
        query_str = "SELECT * FROM Eventos"
        db.delete(db.GqlQuery(query_str))

    def find_By_Id(self, identificador):
      return db.Model.get(identificador)

    def caducado(self):
      if self.fecha_Evento > datetime.datetime.today():
        return True
      else:	
        return False


    def delete_Model(self, evento):
      db.delete(evento)

      if evento:
        return False
      else:
        return True

    #def Cercanos(self,xlat,xlon):
        #query_str = "SELECT * FROM Eventos where lat-"+str(xlat)+"<0.01 AND lon-"+str(xlon)+">-0.01 OR lat-"+str(xlat)+">-0.01 AND lon-"+str(xlon)+"<0.01"
        #return db.GqlQuery(query_str)

