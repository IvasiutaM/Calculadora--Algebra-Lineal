import customtkinter as ctk

# Componente reutilizable para la entrada de matrices
class MatrixInput(ctk.CTkFrame):
    def __init__(self, master, rows, columns):
        super().__init__(master)

        self.rows = rows
        self.columns = columns

        self.entries = []