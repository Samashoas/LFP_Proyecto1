import math
from Abstract.Abstract import OperaGX

class trigonometrica(OperaGX):
    def __init__(self, NumIzq, tipo, fila, columna):
        self.NumIzq = NumIzq
        self.tipo = tipo
        super().__init__(fila, columna)
    def calculadora(self, nodo):
        NI = ''
        if self.NumIzq != None:
            NI = self.NumIzq.calculadora(nodo)
        if self.tipo.calculadora(nodo) == 'Seno':
            resp = math.sin(math.radians(float(NI)))
            return resp
        elif self.tipo.calculadora(nodo) == 'Coseno':
            resp = math.cos(math.radians(float(NI)))
            return resp
        elif self.tipo.calculadora(nodo) == 'Tangente':
            resp = math.tan(math.radians(float(NI)))
            return resp
        else:
            return None
    def get_fila(self):
        return super().get_fila
    def get_column(self):
        return super().get_column
    def getGraphLabel(self):
        return str(self.tipo) + "\\n"+ str(self.operar(None))