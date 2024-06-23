from PyQt6.QtWidgets import QStatusBar, QLabel, QHBoxLayout, QWidget
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt

class Footer:
    """
    Clase que representa el footer de la interfaz.

    Esta clase configura y muestra el footer de la interfaz, que incluye un copyright y un enlace al repositorio.
    """

    def __init__(self, parent):
        """
        Inicializa una nueva instancia de la clase Footer.

        Parameters:
            parent (QWidget): La ventana padre de la interfaz.
        """

        # Crear un nuevo status bar
        self.status_bar = QStatusBar(parent)
        
        # Crear un nuevo contenedor para el footer
        container = QWidget()
        # Establecer el contenedor como el layout del status bar
        layout = QHBoxLayout()
        # Establecer el layout del contenedor
        container.setLayout(layout)
        
        # Añade texto de copyright
        self.copyright_label = QLabel("© 2024 ScrapOps")
        # Establecer el texto de copyright
        layout.addWidget(self.copyright_label)
        
        # Añade un enlace al repositorio
        self.repo_label = QLabel('<a href="https://github.com/Facuud2/Proyecto-P.A-UNAB">Repositorio en GitHub</a>')
        # Establecer el enlace al repositorio
        self.repo_label.setOpenExternalLinks(True)
        # Establecer el cursor
        self.repo_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # Establecer el layout
        layout.addWidget(self.repo_label)
        
        # Añadir el contenedor al status bar
        self.status_bar.addPermanentWidget(container)
    
    def update_message(self, message):
        """
        Parameters:
            message (str): El nuevo mensaje de estado.
        
        Establece el nuevo mensaje de estado.
        """
        self.status_bar.showMessage(message)
    
    def add_widget(self, widget):
        """
        Parameters:
            widget (QWidget): El widget que se agregará al footer.
        
        Agrega un widget al footer.
        """
        self.status_bar.addPermanentWidget(widget)
    
    def get_status_bar(self):
        """
        Returns:
            QStatusBar: El status bar del footer.
        """
        return self.status_bar