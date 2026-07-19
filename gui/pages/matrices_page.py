import customtkinter as ctk


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
            text="Aquí construiremos todas las operaciones con matrices.",
            font=("Segoe UI", 18)
        )

        descripcion.pack()