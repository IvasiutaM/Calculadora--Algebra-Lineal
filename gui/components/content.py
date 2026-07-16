import customtkinter as ctk

class ContentFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(
            self,
            text=(
                "Bienvenido a la calculadora de álgebra lineal\n\n"
                "Seleccione una opción en el menú lateral para comenzar."
            ),
            font=("Segoe UI", 22)
        )

        label.pack(expand=True)