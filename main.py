from pyqt_ui.modules.header import Header
from pyqt_ui.modules.body import Body
from pyqt_ui.modules.footer import Footer
from pyqt_ui.config.config_window import config_window
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal, QObject

import sys

class Communicate(QObject):
    """
    Señal que avisa cuando la data es scrapeada
    """
    data_scraped = pyqtSignal(dict)

class MainWindow(QMainWindow):
    """
    Ventana principal de la app
    """
    def __init__(self):
        """
        Inicializa la ventana principal
        """
        super().__init__()

        # Se da estilo a la ventana
        self.setStyleSheet("""
                        QMainWindow {
                            background-image: url('pyqt_ui/src/background.svg');
                                            background-repeat: no-repeat;
                                            background-position: center;
                                            background-size: cover; 
                        }
                        """)

        # Configura la ventana
        config_window(self)

        # Crea el objeto de comunicación
        self.communicate = Communicate()

        # Crea los layouts de header y body
        header_layout = Header()
        main_layout = Body(self.communicate)
        footer_layout = Footer(self)

        # Establece los layouts en la ventana
        self.setMenuWidget(header_layout)
        self.setCentralWidget(main_layout)
        self.setStatusBar(footer_layout.get_status_bar())
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Conecta la señal de data_scraped al metodo update_data
        self.communicate.data_scraped.connect(main_layout.update_data)

if __name__ == '__main__':
    # Crea la instancia de la aplicación
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
