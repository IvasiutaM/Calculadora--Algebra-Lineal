import customtkinter as ctk

from gui.pages.home_page import HomePage

class ContentFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # Permite que la página ocupe todo el espacio disponible
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Página inicial
        self.current_page = HomePage(self)
        self.current_page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )