'''
Created on 23/11/2013
@author: Juanpa y Yami
'''
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

from colombianCrush.crush import Contenedor

def inicio(request):
    titulo = "COLOMBIAN CRUSH"
    t = get_template("paginaPrincipal.html")
    salida = t.render(Context({'titulo':titulo}))
    return HttpResponse(salida)
    
def juego(request):
    """
    metodo de prueba, puede ser eliminado al implementar la parte orientada a objetos
    """
    contenido = Contenedor(filas=5, columnas=5)
    tabla = []
    tabla.extend(contenido.darContenido())
    t = get_template("colombianCrushGame.html")
    salida = t.render(Context({'tabla':tabla}))
    return HttpResponse(salida)