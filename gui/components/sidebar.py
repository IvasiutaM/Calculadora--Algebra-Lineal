import customtkinter as ctk

class Sidebar(ctk.CTkFrame):

    def __init__(self, master, on_module_selected):
        super().__init__(master, width=250, corner_radius=0)
        self.on_module_selected = on_module_selected 

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
                height=40,
                command=lambda m=module: self.on_module_selected(m)
            )
            button.pack( 
            padx=20,
            pady=6
            )