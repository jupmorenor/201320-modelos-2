'''
Created on 2/12/2013

@author: Juanpa y Yami
'''
from colombianCrush.core import VACIO

class Figura(object):

    def __init__(self, imagen):
        self.imagen = imagen
        self.id = 0
        
    def dibujar(self):
        pass
    
    def __unicode__(self):
        return self.id


class Contenedor(object):
    
    def __init__(self, filas=10, columnas=10):
        self.contenedor = [[VACIO for i in xrange(filas)] for y in xrange(columnas)]
        
    
    def agregarFigura(self, id):
        for figura in self.contenedor[0]:
            if figura is VACIO:
                figura = Figura(id)
        
            