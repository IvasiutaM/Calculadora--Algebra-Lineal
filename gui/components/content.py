import customtkinter as ctk

from gui.pages.home_page import HomePage

from gui.pages.matrices_page import MatriccesPage

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

    def show_page(self, page_name):
            
            # Elimina la página actual
            self.current_page.destroy()

            # Selecciona la nueva página
            if page_name == "Matrices":
                self.current_page = MatricesPage(self)
            else:
                self.current_page = HomePage(self)

            # Muestra la página
            self.current_page.grid(
                 row=0,
                 column=0,
                 sticky="nsew"
            )