from Abstract.Abstract import OperaGX

class error(OperaGX):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
    def calculadora(self, no):
        no_ = f'\t\t"No.": {no}\n'
        desc = '\t\t"Descripcion-Token": {\n'
        lex = f'\t\t\t"Lexema": {self.lexema}\n'
        tipo = f'\t\t\t"Tipo": Error Lexico\n'
        fila = f'\t\t\t"Fila": {self.fila}\n'
        columna = f'\t\t\t"Columna": {self.columna}\n'
        fin = '\t\t}\n'

        return '\t{\n' + no_ + desc + lex + tipo + fila + columna + fin +'\t}'
    def get_fila(self):
        return super().get_fila
    def get_column(self):
        return super().get_column