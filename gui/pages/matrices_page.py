import customtkinter as ctk

from gui.components.matrix_input import MatrixInput

class MatricesPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text="Matrices",
            font=("Segoe UI", 28, "bold")
        )

        titulo.pack(pady=40)

        descripcion = ctk.CTkLabel(
            self,
            text="Bienvenido a la sección de matrices.",
            font=("Segoe UI", 18)
        )

        descripcion.pack()

        self.matrix_input = MatrixInput(
            self, 
            rows=3, 
            columns=3
            )
        
        self.matrix_input.pack(pady=20)