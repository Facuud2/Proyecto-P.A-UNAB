from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QPushButton, QFrame
import json
import subprocess

class Body(QWidget):

    def __init__(self, communicate):
        super().__init__()
        self.communicate = communicate
        self.initUI()
        # Conectar la señal de actualización de datos
        self.communicate.data_scraped.connect(self.update_data)

    def initUI(self):
        self.mainFont = QFont('Playfair Display', 25)
        self.main_layout = QHBoxLayout()

        self.left_layout_widget = QWidget()
        self.left_layout = QVBoxLayout()
        self.left_layout_widget.setLayout(self.left_layout)

        self.right_layout_widget = QWidget()
        self.right_layout = QVBoxLayout()
        self.right_layout_widget.setLayout(self.right_layout)

        self.middle_layout = self.create_middle_layout()

        self.main_layout.addWidget(self.left_layout_widget)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addWidget(self.right_layout_widget)

        self.setLayout(self.main_layout)

        # Cargar datos iniciales
        self.load_data()

    def load_data(self):
        self.load_side_layout(self.left_layout, 'Mercado Libre', 'items_ml.json')
        self.load_side_layout(self.right_layout, 'eBay', 'items_ebay.json')

    def load_side_layout(self, layout, section, data_file):
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft if section == 'Page One' else Qt.AlignmentFlag.AlignRight)

        page_number_label = QLabel(section)
        page_number_label.setFont(self.mainFont)

        container_cards_widget = QWidget()
        container_cards_layout = QVBoxLayout()

        # Carga y filtra los datos
        with open(data_file, 'r', encoding='utf-8') as file:
            items = json.load(file)

        # Filtrar elementos y asegurar que todos los valores sean cadenas
        for item in items:
            titulo = self.sanitize(item.get('nombre', 'Sin nombre'))
            precio = self.sanitize(item.get('precio', 'Sin precio'))
            reputacion_producto = self.sanitize(item.get('reputacionTienda', 'Sin reputación'))
            envioGratis = self.sanitize(item.get('envioGratis', 'No disponible'))

            description = f'''
        Precio: {precio}
        Calificación de usuarios: {reputacion_producto}
        Envío Gratis: {envioGratis}'''

            card = self.create_card(titulo, description)
            container_cards_layout.addWidget(card)

        container_cards_widget.setLayout(container_cards_layout)

        item_scroll_area = QScrollArea()
        item_scroll_area.setWidgetResizable(True)
        item_scroll_area.setWidget(container_cards_widget)

        # Limpiar y actualizar layout
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()
        layout.addWidget(page_number_label)
        layout.addWidget(item_scroll_area)

    def create_middle_layout(self):
        middle_layout = QVBoxLayout()
        middle_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.input_url_label = QLineEdit()
        self.input_url_label.setStyleSheet('border:2px solid; margin-bottom:10px; border-radius: 10px;padding:9px')

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
        button_middle_btn.clicked.connect(self.scrape_data)

        middle_layout.addWidget(self.input_url_label)
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

    def sanitize(self, value):
        """
        Convierte valores a cadena si son listas, asegurando que el valor
        devuelto sea siempre una cadena.
        """
        if isinstance(value, list):
            return ', '.join(value)
        return str(value)

    def scrape_data(self):
        search_item = self.input_url_label.text()

        if search_item:
            ml_command = f"scrapy crawl scrapper_ml -a search={search_item} -o items_ml.json"
            ebay_command = f"scrapy crawl scrapper_ebay -a search={search_item} -o items_ebay.json"

            try:
                subprocess.run(ml_command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")

            try:
                subprocess.run(ebay_command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")

        self.communicate.data_scraped.emit({'search_item': search_item})

    def update_data(self):
        self.load_data()
