import customtkinter as ctk

# Componente reutilizable para la entrada de matrices
class MatrixInput(ctk.CTkFrame):
    def __init__(self, master, rows, columns):
        super().__init__(master)

        self.rows = rows
        self.columns = columns

        self.entries = []

        self._create_grid()
    
    def _create_grid(self): # Crea la grilla de entrada de la matriz
        
        for row in range(self.rows):
            current_row = []

            for column in range(self.columns):
                pass
        
        self.entries.append(current_row)