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
                entry = ctk.CTkEntry(
                    self,
                    width=60,
                    justify="center"
                )

                entry.grid(
                    row=row,
                    column=column,
                    padx=5,
                    pady=5
                )

                current_row.append(entry)
        
        self.entries.append(current_row)