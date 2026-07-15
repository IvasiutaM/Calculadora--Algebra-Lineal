# Archivo responsable de crear la interfaz grafica principal de la calculadora de algebra lineal

import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__() # crea la ventana de CustomTkinter

        self.title("Calculadora de Algebra Lineal")

        self.geometry("900x600") # define el tamaño inicial de la ventana

        self.minsize(800, 500) # evita que el usuario reduzca demasiado la ventana