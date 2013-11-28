from DataBase import DBPublicidad
import datetime


def alta(empresa, url, imagen, lugar, fecha_Vencimiento):
  publicacion = DBPublicidad.Publicidad()#.get_or_insert('nuevo')
  publicacion.empresa = empresa
  publicacion.lugar = lugar
  publicacion.url = url
  publicacion.set_Image(imagen)
  publicacion.fecha_Vencimiento = fecha_Vencimiento
  publicacion.put()


def buscar_Por_Empresa(empresa):
  return DBPublicidad.Publicidad().find_By_Empresa(empresa)

def buscar_Por_Lugar(lugar):
  return DBPublicidad.Publicidad().find_By_Lugar(lugar)

def buscar_Por_Id(identificador):
  return DBPublicidad.Publicidad().find_By_Id(identificador)


def mostrar_Todo():
  return DBPublicidad.Publicidad().get_All()


def borrar_Todo():
  todo = mostrar_Todo()

  for publicacion in todo:
    DBPublicidad.Publicidad().delete_Model(publicacion)


def baja(image_Id):
  publicacion = DBPublicidad.Publicidad().get_or_insert(image_Id)
  if publicacion:
    return DBPublicidad.delete_Model(publicacion)
  else:
    return False


def limpiar_Caducados():
  publicaciones_Todo = DBPublicidad.get_All()

  for publicacion in publicaciones_Todo:
    if publicacion.Publicidad().caducado:
      DBPublicidad.Publicidad().delete_Model(publicacion)

      if publicacion:
        return False

