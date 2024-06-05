from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel


class Header(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        headerFont = QFont('Poppins', 17)

        company_name_label = QLabel('Una Locura TM.')
        dumb_msg_label = QLabel('ScraPy & PyQT babe!')

        company_name_label.setFont(headerFont)
        company_name_label.setStyleSheet("margin-top: 15px; margin-left: 15px;")

        pixmap = QPixmap('../src/klipartz.com.png')
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