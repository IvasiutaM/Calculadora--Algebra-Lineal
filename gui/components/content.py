import customtkinter as ctk

from gui.pages.home_page import HomePage

from gui.pages.matrices_page import MatricesPage

# Definición del diccionario de páginas. Cada clave es el nombre del módulo y el valor es la clase correspondiente a la página.
PAGES = {
    "Matrices": MatricesPage,
}

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

            page_class = PAGES.get(page_name, HomePage) # Get busca la clave en el diccionario y devuelve el valor correspondiente. Si no encuentra la clave, devuelve HomePage como valor predeterminado.

            self.current_page = page_class(self) 

            # Muestra la página
            self.current_page.grid(
                 row=0,
                 column=0,
                 sticky="nsew"
            )