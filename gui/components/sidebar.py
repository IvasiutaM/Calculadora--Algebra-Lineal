import customtkinter as ctk

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=250, corner_radius=0)

        self.grid_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="ÁLGEBRA\nLINEAL",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(pady=(25, 35))

        modules = [
            "Sistemas de ecuaciones",
            "Matrices",
            "Determinantes",
            "Vectores",
            "Grafos",
            "Rectas y planos",
            "Espacios vectoriales",
            "Aplicaciones lineales"
        ]

        for module in modules:

            button = ctk.CTkButton(
                self,
                text=module,
                width=200,
                height=40
            )
            button.pack( 
            padx=20,
            pady=6
            )