import os
from pyswip import Prolog
from random import randint
from django.conf import settings


#CONSTANTES DE IDENTIFICACION DE LOS ESTADOS DEL JUEGO

PASIVO = 0
#Estado en el que el jugador puede hacer su movimiento

ACTIVO = 1
#Estado en el que se reacomodan las fichas 

DESTRUCCION = 2
#Estado en el que se consulta la base de conocimiento para obtener 
#las posibilidades de eliminacion de elementos y se eliminan las fichas posibles

INACTIVO = 3
#Estado en el que se genera una sugerencia para el jugador

#CONSTANTES DE IDENTIFICACION DE LAS FIGURAS
BOMBA_COLOR = 500

VERDE_NORMAL = 501
NARANJA_NORMAL = 502
AMARILLO_NORMAL = 503
MORADO_NORMAL = 504
ROJO_NORMAL = 505
AZUL_NORMAL = 506
#FIGURAS BASICAS RELLENAS

VERDE_RAYAS = 511
NARANJA_RAYAS = 512
AMARILLO_RAYAS = 513
MORADO_RAYAS = 514
ROJO_RAYAS = 515
AZUL_RAYAS = 516
#FIGURAS A RAYAS

VERDE_EMPAQUE = 521
NARANJA_EMPAQUE = 522
AMARILLO_EMPAQUE = 523
MORADO_EMPAQUE = 524
ROJO_EMPAQUE = 525
AZUL_EMPAQUE = 526
#FIGURAS CON EMPAQUE

VACIO = 600

LINEA_5H = 1001
LINEA_5V = 1002
L_ARRIBA_IZQ = 1003
L_ABAJO_IZQ = 1004
L_ABAJO_DER = 1005
L_ARRIBA_DER = 1006
T_ARRIBA = 1007
T_IZQUIERDA = 1008
T_ABAJO = 1009
T_DERECHA = 1010
LINEA_ARRIBA_4 = 1011
LINEA_ABAJO_4 = 1012
LINEA_IZQ_4 = 1013
LINEA_DER_4 = 1014
LINEA_ARRIBA_3 = 1015
LINEA_IZQ_3 = 1016
LINEA_ABAJO_3 = 1017
LINEA_DER_3 = 1018
LINEA_3V = 1019
LINEA_3H = 1020
#CONSTANTES DE IDENTIFICACION DE EVENTOS DE DESTRUCCION DE FIGURAS

SUG_ARRIBA_1 = 2001
SUG_ARRIBA_2 = 2002
SUG_ARRIBA_3 = 2003
SUG_IZQ_1 = 2004
SUG_IZQ_2 = 2005
SUG_IZQ_3 = 2006
SUG_ABAJO_1 = 2007
SUG_ABAJO_2 = 2008
SUG_ABAJO_3 = 2009
SUG_DER_1 = 2010
SUG_DER_2 = 2011
SUG_DER_3 = 2012
SUG_CENT_V1 = 2013
SUG_CENT_V2 = 2014
SUG_CENT_H1 = 2015
SUG_CENT_H2 = 2016
#CONSTANTES DE IDENTIFICACION DE SUGERENCIAS DE MOVIMIENTOS


class Consultor(object):
    """Clase que implementa el mecanismo de consultas a la base de conocimientos usando Prolog"""

    def __init__(self, consulta):
        self.consultor = Prolog()
        self.consultor.consult(os.path.join(settings.MEDIA_ROOT, 'colombianCrush.pl').replace('\\','/'))
        self.consulta = consulta
        self.resultado = []
    
    def buscarSugerencia(self):
        """Genera la respuesta a la consulta de una sugerencia de movimiento para el jugador"""
        return self._validarConsulta(self.consultor.query("buscarSugerencia(X, " + self.consulta + ")"))
    
    def buscarPosibilidad(self):
        """Genera la respuesta a la consulta de una posibilidad de destruccion de figuras"""
        return self._validarConsulta(self.consultor.query("buscarPosibilidad(X, " + self.consulta + ")"))
    
    def _validarConsulta(self, consulta):
        """Metodo interno que extrae el menor valor obtenido de Prolog al consultar la base de conocimiento"""
        for valor in consulta:
            self.resultado.append(valor["X"])
        if len(self.resultado)>PASIVO:
            return min(self.resultado)
        else:
            return PASIVO

class Generador:
    """
    clase que implemente el cargado de imagenes y aleatorizacion de las figuras
    """
    
    def cargarImagen(cls, ubicacion):
        """Genera la url de la imagen en el repositorio a partir del id dado"""
        try:
            imagen = (settings.STATIC_URL + str(ubicacion)+'.png')
        except IOError:
            imagen = ubicacion
        return imagen
    
    cargarImagen = classmethod(cargarImagen)
    
    def siguienteFigura(cls):
        """Genera un numero aleatorio que corresponde con el id de la figura a crear"""
        return randint(VERDE_NORMAL, AZUL_NORMAL)
    
    siguienteFigura = classmethod(siguienteFigura)
    
    def arbolConsultar(cls, args):
        """Retorna la cadena que representa la consulta que se le va a realizar a Prolog"""
        return "arbol(%s, arbol(%s, arbol(%s)), arbol(%s, arbol(%s)), \
        arbol(%s, arbol(%s)), arbol(%s, arbol(%s)))" % tuple(args) # 9 argumentos
    
    arbolConsultar = classmethod(arbolConsultar)
        

#Seccion de pruebas
def _test1():
    consulta = "arbol(1, arbol(1, arbol(1)), arbol(1, arbol(2)), arbol(3, arbol(4)), arbol(1, arbol(2)))"
    obj = Consultor(consulta)
    print obj.buscarPosibilidad()

def _test2():
    consulta = Generador.siguienteFigura()
    #obj = Generador.cargarImagen(consulta)
    print consulta

if __name__ == '__main__':
    _test1()
    _test2()