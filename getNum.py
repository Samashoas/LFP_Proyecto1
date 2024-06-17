from Abstract.Abstract import OperaGX

class Numeros(OperaGX):
    def __init__(self, num, fila, columna):
        self.num = num
        super().__init__(fila, columna)
    def calculadora(self, nodo):
        return self.num
    def get_fila(self):
        return super().get_fila
    def get_column(self):
        return super().get_column
    def getGraphLabel(self):
        return str(self.valor)