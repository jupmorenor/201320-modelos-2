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
        self.espacios = 0
    
    def darContenido(self):
        """Retorna la matriz de figuras para que se muestre en pantalla"""
        return self.contenido
    
    def establecerContenido(self, cont):
        """Guarda la matriz obtenida del request de la pagina"""
        self.contenido = cont
     
    def agregarFigura(self):
        for figura in self.contenido[0]:
            if figura is VACIO:
                figura = Figura(Generador.siguienteFigura())
                self.espacios-=1
                
    def bajarFigura(self):
        self.espacios = 0
        for fila in xrange(len(self.contenido)):
            for fig in xrange(len(self.contenido[0])):
                try:
                    if self.contenido[fila+1][fig] is VACIO:
                        self.contenido[fila+1][fig]=self.contenido[fila][fig]
                        self.contenido[fila][fig]=VACIO
                        self.espacios+=1
                except IndexError:
                    break;

class Controlador(object):
    """Clase que controla el flujo del juego"""

    def __init__(self):
        self.tablero = Contenedor()
        self.estado = ACTIVO
        self.preconsulta = []
        self.consultor = None
        self.respuesta = 0
        self.puntaje = 0
    
    def controlJuego(self):
        if self.estado is ACTIVO:
            self.tablero.bajarFigura()
            while self.tablero.espacios>0:
                self.tablero.bajarFigura()
                self.tablero.agregarFigura()
                if self.tablero.espacios<=0:
                    self.estado = PASIVO
            
        
        elif self.estado is PASIVO:
            pass # turno del jugador
        
        elif self.estado is DESTRUCCION:
            for i in xrange(len(self.tablero.contenido)):
                for j in xrange(len(self.tablero.contenido[0])):
                    try:
                        self.preconsulta.append(self.tablero.contenido[i][j])
                    except IndexError:
                        self.preconsulta.append(200)
                    try:
                        self.preconsulta.append(self.tablero.contenido[i-1][j])
                    except IndexError:
                        self.preconsulta.append(200)
                    try:
                        self.preconsulta.append(self.tablero.contenido[i-2][j])
                    except IndexError:
                        self.preconsulta.append(200)
                    try:
                        self.preconsulta.append(self.tablero.contenido[i][j-1])
                    except IndexError:
                        self.preconsulta.append(200)
                    try:
                        self.preconsulta.append(self.tablero.contenido[i][j-2])
                    except IndexError:
                        self.preconsulta.append(200)
                    try:
                        self.preconsulta.append(self.tablero.contenido[i+1][j])
                    except IndexError:
                        self.preconsulta.append(200)
                    try:
                        self.preconsulta.append(self.tablero.contenido[i+2][j])
                    except IndexError:
                        self.preconsulta.append(200)
                    try:
                        self.preconsulta.append(self.tablero.contenido[i][j+1])
                    except IndexError:
                        self.preconsulta.append(200)
                    try:
                        self.preconsulta.append(self.tablero.contenido[i][j+2])
                    except IndexError:
                        self.preconsulta.append(200)
                    self.consultor = Consultor(Generador.arbolConsultar(self.preconsulta))
                    self.respuesta = self.consultor.buscarPosibilidad()
                    
                    if self.respuesta is PASIVO:
                        self.estado = PASIVO
                    
                    elif self.respuesta is LINEA_5H:
                        self.tablero.contenido[i][j] = Figura(ESTRELLA)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.tablero.contenido[i][j-2] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.tablero.contenido[i][j+2] = Figura(VACIO)
                        self.puntaje += 100
                        self.estado = ACTIVO
                    
                    elif self.respuesta is LINEA_5V:
                        self.tablero.contenido[i][j] = Figura(ESTRELLA)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i-2][j] = Figura(VACIO)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.tablero.contenido[i+2][j] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                        
                    elif self.respuesta is L_ARRIBA_IZQ:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+20)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i-2][j] = Figura(VACIO)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.tablero.contenido[i][j-2] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                    
                    elif self.respuesta is L_ABAJO_IZQ:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+20)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.tablero.contenido[i+2][j] = Figura(VACIO)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.tablero.contenido[i][j-2] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                    
                    elif self.respuesta is L_ABAJO_DER:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+20)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.tablero.contenido[i+2][j] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.tablero.contenido[i][j+2] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                        
                    elif self.respuesta is L_ARRIBA_DER:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+20)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i-2][j] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.tablero.contenido[i][j+2] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                        
                    elif self.respuesta is T_ARRIBA:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+20)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i-2][j] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                        
                    elif self.respuesta is T_IZQUIERDA:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+20)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.tablero.contenido[i][j-2] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                        
                    elif self.respuesta is T_ABAJO:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+20)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.tablero.contenido[i+2][j] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                        
                    elif self.respuesta is T_DERECHA:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+20)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.tablero.contenido[i][j+2] = Figura(VACIO)
                        self.puntaje += 50
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_ARRIBA_4:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+10)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i-2][j] = Figura(VACIO)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.puntaje += 40
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_ABAJO_4:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+10)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i+2][j] = Figura(VACIO)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.puntaje += 40
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_IZQ_4:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+10)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.tablero.contenido[i][j-2] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.puntaje += 40
                        self.estado = ACTIVO
                    
                    elif self.respuesta is LINEA_DER_4:
                        self.tablero.contenido[i][j] = Figura(self.tablero.contenido[i][j]+10)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.tablero.contenido[i][j+2] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.puntaje += 40
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_ARRIBA_3:
                        self.tablero.contenido[i][j] = Figura(VACIO)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.tablero.contenido[i-2][j] = Figura(VACIO)
                        self.puntaje += 30
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_IZQ_3:
                        self.tablero.contenido[i][j] = Figura(VACIO)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.tablero.contenido[i][j-2] = Figura(VACIO)
                        self.puntaje += 30
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_ABAJO_3:
                        self.tablero.contenido[i][j] = Figura(VACIO)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.tablero.contenido[i+2][j] = Figura(VACIO)
                        self.puntaje += 30
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_DER_3:
                        self.tablero.contenido[i][j] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.tablero.contenido[i][j+2] = Figura(VACIO)
                        self.puntaje += 30
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_3V:
                        self.tablero.contenido[i][j] = Figura(VACIO)
                        self.tablero.contenido[i+1][j] = Figura(VACIO)
                        self.tablero.contenido[i-1][j] = Figura(VACIO)
                        self.puntaje += 30
                        self.estado = ACTIVO
                        
                    elif self.respuesta is LINEA_3H:
                        self.tablero.contenido[i][j] = Figura(VACIO)
                        self.tablero.contenido[i][j+1] = Figura(VACIO)
                        self.tablero.contenido[i][j-1] = Figura(VACIO)
                        self.puntaje += 30
                        self.estado = ACTIVO
                    
        elif self.estado is INACTIVO:
            pass
        