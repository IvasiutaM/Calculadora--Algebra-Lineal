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

        self.controls_frame = ctk.CTkFrame(self)

        self.controls_frame.pack(
            pady=20,
            padx=20,
            fill="x"
        )

        self.matrix_area = ctk.CTkFrame(self)

        self.matrix_area.pack(
            fill="both",
            expand=True,
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

        