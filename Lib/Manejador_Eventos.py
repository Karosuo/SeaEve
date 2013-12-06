from DataBase import BDEventos
import datetime


def alta(nombre, imagen, descripcion, contacto, tags, evento_Pagado, fecha_Evento, coordenadas_Mapa, costo, categoria, estado, direccion, organizador, rango_edad):
    	evento = BDEventos.Eventos()
    	evento.nombre = nombre  
        evento.descripcion = descripcion#Descripcion
        evento.contacto = contacto#Diccionario con tupla "redN":"urlN"
        evento.tags = tags
        evento.evento_Pagado = evento_Pagado #true, false
        evento.fecha_Evento = fecha_Evento #cuando se realizara al evento
        evento.set_CoordenadasMapa(coordenadas_Mapa) #coordenadas del mapa, recibe una lista [lt,lg]
        evento.costo = costo #costo del evento
        evento.categoria = categoria #categoria del evento, solo una
        evento.estado = estado #activo o inactivo (no realizado o realizado)
        evento.direccion = direccion #Texto definiendo la direccion como tal
        evento.organizador = organizador
        evento.rango_Edad = rango_Edad
        evento.set_Image(imagen)


def buscar_Por_Id(identificador):
	return BDEventos.Eventos().find_By_Id(identificador)


def mostrar_Todo():
	return BDEventos.Eventos().All()

def borrar_Todo():
	return BDEventos.Eventos().DeleteAll()
	