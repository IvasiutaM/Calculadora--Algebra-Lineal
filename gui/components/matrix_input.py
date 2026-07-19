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
    
    def get_matrix(self): # Obtiene la matriz ingresada por el usuario
        matrix = []

        for row in self.entries:
            current_row = []

            for entry in row:

                value = entry.get()

                current_row.append(float(value))
            
            matrix.append(current_row)
        
        return matrix