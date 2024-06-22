from pyqt_ui.modules.header import Header
from pyqt_ui.modules.body import Body
# from pyqt_ui.modules.footer import Footer
from pyqt_ui.config.config_window import config_window
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal, QObject

import sys

class Communicate(QObject):
    data_scraped = pyqtSignal(dict)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
                        QMainWindow {
                            background-image: url('pyqt_ui/src/background.svg');
                                            background-repeat: no-repeat;
                                            background-position: center;
                                            background-size: cover; 
                        }

                                    """)
        config_window(self)

        self.communicate = Communicate()

        header_layout = Header()
        main_layout = Body(self.communicate)
        # footer_layout = Footer()

        self.setMenuWidget(header_layout)
        self.setCentralWidget(main_layout)
        # self.statusBar().addWidget(footer_layout)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Conectar la señal
        self.communicate.data_scraped.connect(main_layout.update_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # No olvides mostrar la ventana
    sys.exit(app.exec())
