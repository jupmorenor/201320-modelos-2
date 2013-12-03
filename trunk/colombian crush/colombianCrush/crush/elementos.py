'''
Created on 2/12/2013

@author: Juanpa y Yami
'''
from colombianCrush.core import VACIO, Generador

class Figura(object):

    def __init__(self, imagen):
        self.id = imagen
        self.imagen = Generador.cargarImagen(imagen)
        
    def dibujar(self):
        pass
    
    def __unicode__(self):
        return self.id


class Contenedor(object):
    
    def __init__(self, filas=10, columnas=10):
        self.contenido = [[VACIO for i in xrange(filas)] for y in xrange(columnas)]
    
    def darContenido(self):
        print type(self.contenido)
        return self.contenido
     
    def agregarFigura(self):
        for figura in self.contenido[0]:
            if figura is VACIO:
                figura = Figura(Generador.siguienteFigura())
                
    def bajarFigura(self):
        for fila in xrange(len(self.contenido)):
            for fig in xrange(len(self.contenido[0])):
                try:
                    if self.contenido[fila+1][fig] is VACIO:
                        self.contenido[fila+1][fig]=self.contenido[fila][fig]
                        self.contenido[fila][fig]=VACIO
                except IndexError:
                    pass
