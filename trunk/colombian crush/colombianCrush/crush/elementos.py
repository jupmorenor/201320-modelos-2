'''
Created on 2/12/2013

@author: Juanpa y Yami
'''
from colombianCrush.core import *

class Figura(object):
    """Clase que representa a una figura que se puede ver en pantalla"""

    def __init__(self, imagen):
        self.id = imagen
        self.imagen = Generador.cargarImagen(imagen)
        
    def dibujar(self):
        """Retorna la url de la imagen de la figura para que sea dibujada"""
        return self.imagen
    
    def __unicode__(self):
        return self.id


class Contenedor(object):
    """Clase que contiene la matriz de figuras que se ve en pantalla"""
    
    def __init__(self, filas=10, columnas=10):
        self.contenido = [[Figura(Generador.siguienteFigura()) for i in xrange(filas)] for y in xrange(columnas)]
    
    def darContenido(self):
        """Retorna la matriz de figuras para que se muestre en pantalla"""
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

class Controlador(object):
    """Clase que controla el flujo del juego"""

    def __init__(self):
        self.estado = ACTIVO
    
    def controlJuego(self):
        if self.estado is ACTIVO:
            pass
        
        elif self.estado is PASIVO:
            pass
        
        elif self.estado is DESTRUCCION:
            pass
        
        elif self.estado is INACTIVO:
            pass
        