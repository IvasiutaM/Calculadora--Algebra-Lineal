import customtkinter as ctk
from matplotlib.pylab import matrix

from gui.components.matrix_input import MatrixInput

class MatricesPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self._create_header()
        self._create_layout()
        self._create_controls()

    def _create_header(self): # Crea el encabezado de la página
        titulo = ctk.CTkLabel(
            self,
            text="Matrices",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=(20,5))

        descripcion = ctk.CTkLabel(
            self,
            text="Realiza operaciones entre matrices y visualiza el procedimiento paso a paso.",
            justify="center"
        )

        descripcion.pack(pady=(0,20))
    
    def _create_layout(self): # Crea la estructura de la página
        self.controls_frame = ctk.CTkFrame(self)

        self.controls_frame.pack(
            pady=20,
            padx=20,
            fill="x"
        )

        self.matrix_area = ctk.CTkFrame(self)

        self.matrix_area.pack(
            fill="both",
            padx=20,
            pady=10
        )

        self.operations_frame = ctk.CTkFrame(self)

        self.operations_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.result_frame = ctk.CTkFrame(self)

        self.result_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.procedure_frame = ctk.CTkFrame(self)

        self.procedure_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10,20)
        )
    
    def _create_controls(self): # Crea los controles de configuración
        section_title = ctk.CTkLabel(
            self.controls_frame,
            text="Configuración",
            font=("Segoe UI", 18, "bold")
        )

        section_title.pack(
            anchor="w",
            padx=15,
            pady=(15,10)
        )

        form_frame = ctk.CTkFrame(
            self.controls_frame,
            fg_color="transparent"
        )

        form_frame.pack(
            padx=15,
            pady=(0,15),
            anchor="w"
        )

        rows_label = ctk.CTkLabel(
            form_frame,
            text="Filas:"
        )

        rows_label.grid(
            row=1,
            column=0,
            padx=(0,20),
            pady=5,
            sticky="w"
        )

        self.rows_combobox = ctk.CTkComboBox(
            form_frame,
            values=["2", "3", "4", "5", "6"]
        )

        self.rows_combobox.grid(
            row=1,
            column=1,
            pady=5
        )

        self.rows_combobox.set("3")