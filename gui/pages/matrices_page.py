import customtkinter as ctk
from matplotlib.pylab import matrix

from gui.components.matrix_input import MatrixInput

class MatricesPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # Lista donde se guardarán las matrices creadas
        self.matrix_inputs = []

        self._create_header()
        self._create_layout()
        self._create_controls()

    def _create_header(self): # Crea el encabezado de la página

        titulo = ctk.CTkLabel(
            self,
            text="Matrices",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=(20, 5))

        descripcion = ctk.CTkLabel(
            self,
            text="Realiza operaciones entre matrices y visualiza el procedimiento paso a paso.",
            justify="center"
        )

        descripcion.pack(pady=(0, 20))

    def _create_layout(self): # Crea la estructura principal de la página

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
            pady=(10, 20)
        )

    def _create_controls(self): # Crea los controles de configuración

        section_title = ctk.CTkLabel(
            self.controls_frame,
            text="Configuración",
            font=("Segoe UI", 18, "bold")
        )

        section_title.pack( # Título
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        form_frame = ctk.CTkFrame( # Formulario
            self.controls_frame,
            fg_color="transparent"
        )

        form_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        rows_label = ctk.CTkLabel( # Etiquetas
            form_frame,
            text="Filas"
        )

        rows_label.grid(
            row=0,
            column=0,
            padx=10,
            sticky="w"
        )

        columns_label = ctk.CTkLabel(
            form_frame,
            text="Columnas"
        )

        columns_label.grid(
            row=0,
            column=1,
            padx=10,
            sticky="w"
        )

        quantity_label = ctk.CTkLabel(
            form_frame,
            text="Cantidad de matrices"
        )

        quantity_label.grid(
            row=0,
            column=2,
            padx=10,
            sticky="w"
        )

        self.rows_combobox = ctk.CTkComboBox( # Combobox Filas
            form_frame,
            values=["2", "3", "4", "5", "6"],
            width=90
        )

        self.rows_combobox.grid(
            row=1,
            column=0,
            padx=10,
            pady=(5, 0)
        )

        self.rows_combobox.set("3")

        self.columns_combobox = ctk.CTkComboBox( # Combobox Columnas
            form_frame,
            values=["2", "3", "4", "5", "6"],
            width=90
        )

        self.columns_combobox.grid(
            row=1,
            column=1,
            padx=10,
            pady=(5, 0)
        )

        self.columns_combobox.set("3")

        self.quantity_combobox = ctk.CTkComboBox( # Combobox Cantidad
            form_frame,
            values=["2", "3", "4", "5"],
            width=140
        )

        self.quantity_combobox.grid(
            row=1,
            column=2,
            padx=10,
            pady=(5, 0)
        )

        self.quantity_combobox.set("2")

        self.create_button = ctk.CTkButton( # Botón
            form_frame,
            text="Crear matrices",
            command=self._create_matrices
        )

        self.create_button.grid(
            row=1,
            column=3,
            padx=(30, 0),
            pady=(5, 0)
        )

    # Eventos
    def _create_matrices(self): # Lee la configuración seleccionada

        rows = int(self.rows_combobox.get())
        columns = int(self.columns_combobox.get())
        quantity = int(self.quantity_combobox.get())

        print("=== CONFIGURACIÓN ===")
        print(f"Filas: {rows}")
        print(f"Columnas: {columns}")
        print(f"Cantidad: {quantity}")