'''
Created on 23/11/2013
@author: Juanpa y Yami
'''
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

def test(request):
    """
    metodo de prueba, puede ser eliminado al implementar la parte orientada a objetos
    """
    t = get_template("colombianCrushGame.html")
    salida = t.render(Context({}))
    return HttpResponse(salida)