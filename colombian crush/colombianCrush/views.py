'''
Created on 23/11/2013
@author: Juanpa y Yami
'''
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

from colombianCrush.crush import Contenedor, Figura

def inicio(request):
    """Metodo que envia la pagina principal del juego"""
    titulo = "COLOMBIAN CRUSH"
    imagen = Figura(500)
    t = get_template("paginaPrincipal.html")
    salida = t.render(Context({'imagen':imagen.dibujar(), 'titulo':titulo}))
    return HttpResponse(salida)
    
def juego(request):
    """Metodo que envia el contenido del juego a la ventana"""
    contenido = Contenedor()
    tabla = []
    tabla.extend(contenido.darContenido())
    t = get_template("colombianCrushGame.html")
    salida = t.render(Context({'tabla':tabla}))
    return HttpResponse(salida)