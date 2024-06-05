from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QPushButton, QFrame
import json


class Body(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        mainFont = QFont('Playfair Display', 25)
        main_layout = QHBoxLayout()

        left_layout = self.create_side_layout(mainFont,'Page One', 'items_ml.json')
        right_layout = self.create_side_layout(mainFont,'Page Two', 'items_ebay.json')
        middle_layout = self.create_middle_layout()

        main_layout.addLayout(left_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(right_layout)


        self.setLayout(main_layout)

    def create_side_layout(self, mainFont, section, data_file):
        side_layout = QVBoxLayout()
        side_layout.setAlignment(Qt.AlignmentFlag.AlignLeft if section == 'Page One' else Qt.AlignmentFlag.AlignRight)

        page_number_label = QLabel(section)
        page_number_label.setFont(mainFont)

        input_url_label = QLineEdit()
        input_url_label.setStyleSheet('border:2px solid; margin-bottom:10px; border-radius: 10px;padding:9px')

        container_cards_widget = QWidget()
        container_cards_layout = QVBoxLayout()

        with open(data_file, 'r') as file:
            items = json.load(file)

        for item in items:
            titulo = item['nombre']
            precio = item['precio']
            reputacion_producto = item['reputacionTienda']
            envioGratis = item['envioGratis']
            description = f'''
        Precio: {precio}
        Calificacion de usuarios: {reputacion_producto}
        Envio Gratis: {envioGratis}'''

            card = self.create_card(f'{titulo}', description)
            container_cards_layout.addWidget(card)

        container_cards_widget.setLayout(container_cards_layout)

        item_scroll_area = QScrollArea()
        item_scroll_area.setWidgetResizable(True)
        item_scroll_area.setWidget(container_cards_widget)

        side_layout.addWidget(page_number_label)
        side_layout.addWidget(input_url_label,
                              alignment=Qt.AlignmentFlag.AlignLeft if section == "Page One" else Qt.AlignmentFlag.AlignRight)
        side_layout.addWidget(item_scroll_area)

        return side_layout

    def create_middle_layout(self):
        middle_layout = QVBoxLayout()
        middle_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        button_middle_btn = QPushButton('Scrap')
        button_middle_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff6666;
                border: 2px solid #ff6666;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #ff4d4d;
                border: 2px solid #ff4d4d;
                cursor: pointer;
            }
            QPushButton:pressed {
                background-color: #e63939;
                border: 2px solid #e63939;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                border: 2px solid #cccccc;
                color: #666666;
            }
        """)
        middle_layout.addWidget(button_middle_btn)

        return middle_layout

    def create_card(self, item_name, item_content):
        card_frame = QFrame()
        card_frame.setFrameShape(QFrame.Shape.Box)
        card_frame.setLineWidth(2)
        card_frame.setStyleSheet("background-color: #f0f0f0")

        item_name_label = QLabel(item_name)
        item_name_label.setStyleSheet("font-weight: bold; font-size: 18px;")

        item_content_label = QLabel(item_content)
        item_content_label.setFont(QFont('Calibri', 14))

        card_layout = QVBoxLayout()
        card_layout.addWidget(item_name_label)
        card_layout.addWidget(item_content_label)
        card_layout.setContentsMargins(10, 10, 10, 10)
        card_frame.setLayout(card_layout)

        return card_frame

