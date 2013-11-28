from google.appengine.ext import db
#from google.appengine.api import images
import datetime

class Publicidad(db.Model):

  empresa = db.StringProperty() #Nombre de la empresa
  url = db.StringProperty() #URL de sitio destino publicitado
  imagen = db.BlobProperty() #Imagen, slide, etc publicitario.
  lugar = db.StringListProperty() #Ubicacion de la empresa? o del lugar pubilcado (mas probable)...
  fecha_Ingreso = db.DateTimeProperty(auto_now_add = True)
  fecha_Vencimiento = db.DateTimeProperty()

  def set_Image(self, nueva_Imagen):
    #imagen = images.rezise(nueva_Imagen, 150, 150)
    self.imagen = db.Blob(nueva_Imagen)


  def get_All(self):
    gql_Query = 'SELECT * FROM Publicidad'
    return db.GqlQuery(gql_Query)

  def find_By_Empresa(self, empresa):
    gql_Query = 'SELECT * FROM Publicidad WHERE empresa= :empresa'
    return db.GqlQuery(gql_Query, empresa)

  def find_By_Lugar(self, lugar):
    gql_Query = 'SELECT * FROM Publicidad WHERE lugar= :lugar'
    return db.GqlQuery(gql_Query, lugar)


  def find_By_Id(self, identificador):
    return db.Model.get(identificador)

  def caducado(self):
    if self.fecha_Vencimiento == datetime.datetime.today():
      return True
    else:
      return False


  def delete_Model(self, publicacion):
    db.delete(publicacion)

    if publicacion:
      return False
    else:
      return True



