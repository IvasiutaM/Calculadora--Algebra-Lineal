import customtkinter as ctk

from gui.components.sidebar import Sidebar
from gui.components.content import ContentFrame


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Calculadora de Álgebra Lineal")

        self.geometry("1100x700")

        self.minsize(900, 600)

        ctk.set_appearance_mode("System")

        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.content = ContentFrame(self)

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )