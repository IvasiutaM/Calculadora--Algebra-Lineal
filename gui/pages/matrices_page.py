import customtkinter as ctk
from matplotlib.pylab import matrix

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

        self.read_button = ctk.CTkButton(
            self,
            text="Leer matriz",
            command=self.read_matrix
        )

        self.read_button.pack(pady=10)
    
    def read_matrix(self):
        matrix = self.matrix_input.get_matrix()

        print(matrix)