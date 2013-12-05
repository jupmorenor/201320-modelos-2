'''
Created on 23/11/2013
@author: Juanpa y Yami
'''
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect

from colombianCrush.crush import Controlador, Figura
from django.views.decorators.csrf import csrf_protect

contenido = Controlador()

def inicio(request):
    """Metodo que envia la pagina principal del juego"""
    titulo = "COLOMBIAN CRUSH"
    imagen = Figura(500)
    t = get_template("paginaPrincipal.html")
    salida = t.render(Context({'imagen':imagen.dibujar(), 'titulo':titulo}))
    return HttpResponse(salida)

@csrf_protect  
def juego(request):
    """Metodo que envia el contenido del juego a la ventana"""
    if request.method == 'POST':
        contenido.tablero.establecerContenido(request.POST.getlist('tablero[]'))
        contenido.estado = 2
        contenido.controlJuego()
    t = get_template("colombianCrushGame.html")
    salida = t.render(RequestContext(request, {'tabla':contenido.tablero.darContenido(), 'puntaje':contenido.puntaje}))
    return HttpResponse(salida)
    if contenido.puntaje>=1000:
        return HttpResponseRedirect('/fin')

def fin(request):
    t = get_template("despedida.html")
    salida = t.render(Context({'puntaje':contenido.puntaje}))
    return HttpResponse(salida)