import customtkinter as ctk

class HomePage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Calculadora de Álgebra Lineal",
            font=("Segoe UI", 28, "bold")
        )
        
        title.pack(pady=(40,20))

        subtitle = ctk.CTkLabel(
            self,
            text=(
                "Bienvenido.\n\n"
                "Seleccione un módulo del menú lateral para comenzar"
            ),
            font=("Segoe UI", 18)
        )
        subtitle.pack()