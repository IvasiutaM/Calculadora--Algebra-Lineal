# Archivo responsable de crear la interfaz grafica de la calculadora de algebra lineal

import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__() # crea la ventana de CustomTkinter

        # Configuración de la ventana
        self.title("Calculadora de Algebra Lineal")
        self.geometry("900x600") # define el tamaño inicial de la ventana
        self.minsize(800, 500) # evita que el usuario reduzca demasiado la ventana

        # Configuración del tema y color de la ventana

        ctk.set_appearance_mode("System") # establece el modo de apariencia del sistema operativo
        ctk.set_default_color_theme("blue") # establece el tema de colores por defecto

        # Configuración de la cuadrícula principal

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # === Panel lateral ===
        
        self.sidebar = ctk.CTkFrame(
            self, 
            width=250, 
            corner_radius=0
        )

        self.sidebar.grid(
            row=0, 
            column=0, 
            sticky="ns"
        )

        # === Área principal ===

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(
            row=0, 
            column=1, 
            sticky="nsew", 
            padx=20, 
            pady=20
        )

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Título de la calculadora

        self.title_label = ctk.CTkLabel(
            self.sidebar,
            text="ÁLGEBRA\nLINEAL",
            font=("Segoe UI", 22, "bold")
        )

        self.title_label.pack(
            pady=(25,35)
        )

        # Botones
        self.modules = [
            "Sistemas de ecuaciones",
            "Matrices",
            "Determinantes",
            "Vectores",
            "Grafos",
            "Rectas y planos",
            "Espacios vectoriales",
            "Aplicaciones lineales"
        ]

        for module in self.modules:

            button = ctk.CTkButton(
                self.sidebar,
                text=module,
                width=200,
                height=40
            )

        # Mensaje principal
        self.welcome = ctk.CTkLabel(
            self.main_frame,
            text=(
                "Bienvenido a la Calculadora de Álgebra Lineal.\n\n"
                "Seleccione un módulo en el panel lateral para comenzar."
            ),
            font=("Segoe UI", 22)
        )

        self.welcome.pack(expand=True)