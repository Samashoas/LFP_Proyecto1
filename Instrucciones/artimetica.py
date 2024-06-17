from Abstract.Abstract import OperaGX

class Aritmetica(OperaGX):
    def __init__(self, NumIzq, NumDec, tipo,  fila, columna):
        self.NumIzq = NumIzq
        self.NumDec = NumDec
        self.tipo = tipo
        super().__init__(fila, columna)
    def calculadora(self, nodo):
        NI = ''
        ND = ''
        if self.NumIzq != None:
            NI = self.NumIzq.calculadora(nodo)
        if self.NumDec != None:
            ND = self.NumDec.calculadora(nodo)
        if self.tipo.calculadora(nodo) == 'Suma':
            return float(NI) + float(ND)
        elif self.tipo.calculadora(nodo) == 'Resta':
            return float(NI) - float(ND)
        elif self.tipo.calculadora(nodo) == 'Multiplicacion':
            return float(NI) * float(ND)
        elif self.tipo.calculadora(nodo) == 'Division':
            return float(NI) / float(ND)
        elif self.tipo.calculadora(nodo) == 'Modulo':
            return float(NI) % float(ND)
        elif self.tipo.calculadora(nodo) == 'Potencia':
            return float(NI) ** float(ND)
        elif self.tipo.calculadora(nodo) == 'Raiz':
            return float(NI) ** (1/float(ND))
        elif self.tipo.calculadora(nodo) == 'Inverso':
            return 1/float(NI)
        else:
            return None  
    def get_fila(self):
        return super().get_fila
    def get_column(self):
        return super().get_column
    def getGraphLabel(self):
        return str(self.tipo) + "\\n"+ str(self.operar(None))