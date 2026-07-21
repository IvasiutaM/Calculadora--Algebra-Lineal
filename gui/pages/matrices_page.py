import customtkinter as ctk
from matplotlib.pylab import matrix

from gui.components.matrix_input import MatrixInput

class MatricesPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self._create_header()
        self._create_layout()

    def _create_header(self): # Crea el encabezado de la página
        titulo = ctk.CTkLabel(
            self,
            text="Matrices",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=(20,5))

        descripcion = ctk.CTkLabel(
            self,
            text="Realiza operaciones entre matrices y visualiza el procedimiento paso a paso.",
            justify="center"
        )

        descripcion.pack(pady=(0,20))
    
    def _create_layout(self): # Crea la estructura de la página
        self.controls_frame = ctk.CTkFrame(self)

        self.controls_frame.pack(
            pady=20,
            padx=20,
            fill="x"
        )

        self.matrix_area = ctk.CTkFrame(self)

        self.matrix_area.pack(
            fill="both",
            padx=20,
            pady=10
        )

        self.operations_frame = ctk.CTkFrame(self)

        self.operations_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.result_frame = ctk.CTkFrame(self)

        self.result_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.procedure_frame = ctk.CTkFrame(self)

        self.procedure_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10,20)
        )