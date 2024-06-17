from Abstract.Abstract import OperaGX

class Lex(OperaGX):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
    def calculadora(self, nodo):
        return self.lexema
    def get_fila(self):
        return super().get_fila
    def get_column(self):
        return super().get_column