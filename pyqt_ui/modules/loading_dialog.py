from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtCore import Qt

class LoadingDialog(QDialog):
    """
    Clase que representa la ventana que contiene la barra de carga.
    """
    def __init__(self):
        """
        Iniciliza una nueva instancia de la clase LoadingDialog.
        """
        super().__init__()
        # Establece el tiúlo y propiedades de la ventana
        self.setWindowTitle("Cargando")
        self.setModal(True)
        self.setFixedSize(300, 100)

        # Crea el layout y configura su alineamiento
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Crea y configura la etiqueta
        self.label = QLabel("Scraping en progreso, por favor espere...")
        
        # Crea y configura el progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)

        # Agrega la etiqueta y el progress bar al layout
        layout.addWidget(self.label)
        layout.addWidget(self.progress_bar)

        # Establece el layout para la ventana
        self.setLayout(layout)

