import tkinter as tk
from tkinter import filedialog, Tk
from analizador import *
import os
import subprocess

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de Texto")

        self.menu_principal = tk.Menu(self.master)

        self.menu_archivo = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        self.menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        self.menu_archivo.add_command(label="Guardar como", command=self.guardar_archivo_como)
        self.menu_archivo.add_command(label="Analizar", command=self.analizar_texto)
        self.menu_archivo.add_command(label="Errores", command=self.mostrar_errores)
        self.menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_principal.add_cascade(label="Archivo", menu=self.menu_archivo)

        self.master.config(menu=self.menu_principal)

    def abrir_archivo(self):
        self.ruta = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if self.ruta is not None:
            self.archivo = open(self.ruta,'r')
            contenido = self.archivo.read()
            self.texto.delete(1.0, tk.END)
            self.texto.insert(tk.END, contenido)

    
    def guardar_archivo(self):
        if self.ruta is not None:
            with open(self.ruta, "w") as archivo:
                contenido = self.texto.get(1.0, tk.END)
                archivo.write(contenido)

    def guardar_archivo_como(self):
        archivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo is not None:
            contenido = self.texto.get(1.0, tk.END)
            archivo.write(contenido)
            archivo.close()

    def analizar_texto(self):
        archivo = open(self.ruta, "r")
        contenido = archivo.read()
        instruccion(contenido)
        respuestas = calculadora_()
        for respuesta in respuestas:
            print(respuesta.calculadora(None))

    def mostrar_errores(self):
        lista_errores = getErrores()
        contador = 1
        with open('ERRORES_202109705.txt', 'w') as outfile:
            outfile.write('{\n')
            while lista_errores:
                error = lista_errores.pop(0)
                outfile.write(str(error.calculadora(contador)) + ',\n')
                contador +=1
            outfile.write('}')

    def salir(self):
        self.master.destroy()

    def start(self):
        self.texto = tk.Text(self.master)
        self.texto.pack()

def ayuda():
    ventanaAyuda = tk.Toplevel(ventana)
    ventanaAyuda.geometry("400x180")

    etiqueta1 = tk.Label(ventanaAyuda, text="Juan Pablo Samayoa Ruiz", font=("Arial", 16), fg="blue")
    etiqueta1.pack(padx=10, pady=10)

    etiqueta2 = tk.Label(ventanaAyuda, text="202109705", font=("Arial", 16), fg="blue")
    etiqueta2.pack(padx=10, pady=10)

    etiqueta2 = tk.Label(ventanaAyuda, text="Laboratorio LFP B-", font=("Arial", 16), fg="blue")
    etiqueta2.pack(padx=10, pady=10)

def Monstrar_MU():
    ruta_pdf = "C:/Users/jpsam/OneDrive/Escritorio/Python/LFP P1_202109705/[LFP]202109705_Manual de usuario.pdf"
    if os.name == 'nt':
        os.startfile(ruta_pdf)
    else: 
        subprocess.call(["xdg-open", ruta_pdf])

def Monstrar_MT():
    ruta_pdf = "C:/Users/jpsam/OneDrive/Escritorio/Python/LFP P1_202109705/[LFP]202109705_Manual tecnico.pdf"
    if os.name == 'nt':
        os.startfile(ruta_pdf)
    else: 
        subprocess.call(["xdg-open", ruta_pdf])

ventana = tk.Tk()
ventana.geometry("350x250")
ventana.title("Inicio")

marco_principal = tk.Frame(ventana, width=400, height=300)
marco_principal.grid(row=0, column=0, padx=20, pady=20)

menu_archivo = tk.Label(marco_principal, text="Archivo")
menu_archivo.grid(row=0, column=0, padx=10, pady=10)

def abrir_editor():
    editor = TextEditor(tk.Toplevel(ventana))
    editor.start()

boton_abrir = tk.Button(marco_principal, text="Abrir editor de texto", command=abrir_editor)
boton_abrir.grid(row=1, column=0, padx=10, pady=10)

menu_ayuda = tk.Label(marco_principal, text="Ayuda")
menu_ayuda.grid(row=0, column=1, padx=10, pady=10)

boton_manual_usuario = tk.Button(marco_principal, text="Manual usuario", command=Monstrar_MU)
boton_manual_usuario.grid(row=1, column=1, padx=10, pady=10)

boton_manual_ayuda = tk.Button(marco_principal, text="Manual Tecnico", command=Monstrar_MT)
boton_manual_ayuda.grid(row=2, column=1, padx=10, pady=10)

boton_temas = tk.Button(marco_principal, text="Temas de ayuda", command=ayuda)
boton_temas.grid(row=3, column=1, padx=10, pady=10)

ventana.mainloop()
