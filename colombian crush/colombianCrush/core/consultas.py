from pyswip import Prolog

#CONSTANTES DE IDENTIFICACION DE LAS FIGURAS
ESTRELLA = 500

#FIGURAS BASICAS RELLENAS
CUADRO_NEGRO = 501
TRIANGULO_NEGRO = 502
CIRCULO_NEGRO = 503
ROMBO_NEGRO = 504
PENTAGONO_NEGRO = 505
HEXAGONO_NEGRO = 506

#FIGURAS A RAYAS
CUADRO_RAYAS = 511
TRIANGULO_RAYAS = 512
CIRCULO_RAYAS = 513
ROMBO_RAYAS = 514
PENTAGONO_RAYAS = 515
HEXAGONO_RAYAS = 516

#FIGURAS CON FIGURA INTERNA
CUADRO_SUBC = 521
TRIANGULO_SUBT = 522
CIRCULO_SUBCIR = 523
ROMBO_SUBR = 524
PENTAGONO_SUBP = 525
HEXAGONO_SUBH = 526

#CONSTANTES DE IDENTIFICACION DE EVENTOS DE DESTRUCCION DE FIGURAS
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

#CONSTANTES DE IDENTIFICACION DE SUGERENCIAS DE MOVIMIENTOS
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



class Consultor(object):

    def __init__(self, consulta):
        self.consultor = Prolog()
        self.consultor.consult("colombianCrush.pl")
        self.consulta = consulta
        self.resultado = []
    
    def buscarSugerencia(self):
        return self._validarConsulta(self.consultor.query("buscarSugerencia(X, " + self.consulta + ")"))
    
    def buscarPosibilidad(self):
        return self._validarConsulta(self.consultor.query("buscarPosibilidad(X, " + self.consulta + ")"))
    
    def _validarConsulta(self, consulta):
        for valor in consulta:
            self.resultado.append(valor["X"])
        if len(self.resultado)>0:
            return min(self.resultado)
        else:
            return 0
        

def _test():
    consulta =  "buscarPosibilidad(X, arbol(1, arbol(1, arbol(1)), arbol(1, arbol(2)), arbol(3, arbol(4)), arbol(1, arbol(2))))"
    obj = Consultor(consulta)
    print obj.buscarSugerencia()
    