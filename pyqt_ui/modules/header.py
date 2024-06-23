from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel


class Header(QWidget):
    """
    Clase Header que representa la cabecera de la aplicación.

    Esta clase configura y muestra la cabecera de la aplicación, que incluye
    el nombre de la empresa, un logo y un mensaje.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Header.

        Configura el diseño y los elementos de la cabecera, incluyendo el nombre
        de la empresa, un logo y un mensaje.
        """

        super().__init__()

        # Configuración del layout horizontal
        layout = QHBoxLayout()
        # Fuente para el texto de la cabecera
        headerFont = QFont('Poppins', 17)

        # Etiqueta con el nombre de la empresa
        company_name_label = QLabel('Una Locura TM.')
        company_name_label.setFont(headerFont)
        company_name_label.setStyleSheet("margin-top: 15px; margin-left: 15px;")

        # Logo de la empresa
        pixmap = QPixmap('../src/klipartz.com.png')
        logo = QLabel(self)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        logo.setStyleSheet('margin-top:15px')
        # logo.resize()

        # Mensaje en la cabecera
        dumb_msg_label = QLabel('ScraPy & PyQT babe!')
        dumb_msg_label.setFont(headerFont)
        dumb_msg_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        dumb_msg_label.setStyleSheet("margin-top: 15px; margin-right: 15px;")

        # Añadir widgets al layout
        layout.addWidget(company_name_label)
        layout.addWidget(logo)
        layout.addWidget(dumb_msg_label)

        # Establecer el layout para el widget
        self.setLayout(layout)