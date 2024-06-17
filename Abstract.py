from abc import ABC, abstractmethod

class OperaGX(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
    @abstractmethod
    def calculadora(self, nodo):
        pass
    def get_text(self, nodo):
        pass
    @abstractmethod
    def get_fila(self):
        return self.fila
    @abstractmethod
    def get_column(self):
        return self.columna
    def get_node(self):
        return 'n'+str(self.contador)+str(self.contGraph)
    def get_nodeDef(self, index, cluster):
        self.contador = index
        self.contGraph = cluster
        return self.getGraphnode() + " [ shape=note, style=filled, fillcolor=\"#82589F\", label=""+ self.getGraphLabel() + ""]; \n"