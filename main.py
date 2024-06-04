from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QHBoxLayout, \
    QGridLayout, QMainWindow, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap
import sys


class Header(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        headerFont = QFont('Poppins', 17)

        company_name_label = QLabel('Una Locura TM.')
        dumb_msg_label = QLabel('ScraPy & PyQT babe!')

        company_name_label.setFont(headerFont)
        company_name_label.setStyleSheet("margin-top: 15px; margin-left: 15px;")

        pixmap = QPixmap('../pyqt_ui/src/klipartz.com.png')
        logo = QLabel(self)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        logo.setStyleSheet('margin-top:15px')
        # logo.resize()

        dumb_msg_label.setFont(headerFont)
        dumb_msg_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        dumb_msg_label.setStyleSheet("margin-top: 15px; margin-right: 15px;")

        layout.addWidget(company_name_label)
        layout.addWidget(logo)
        layout.addWidget(dumb_msg_label)


        self.setLayout(layout)

class Main(QWidget):
    def __init__(self):
        super().__init__()
        mainFont = QFont('Playfair Display',25)




class Footer(QWidget):
    pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config_window()

        header_layout = Header()
        main_layout = Main()
        footer_layout = Footer()

        self.setMenuWidget(header_layout)
        self.setCentralWidget(main_layout)
        self.statusBar().addWidget(footer_layout)

    def config_window(self):
        self.setWindowTitle('ScrapOps')
        self.setGeometry(300,500,1024,768)
        self.show()
        screen_geometry = self.screen().geometry()
        window_geometry = self.geometry()

        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2

        self.move(x, y)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
