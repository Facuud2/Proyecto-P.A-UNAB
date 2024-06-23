from PyQt6.QtCore import QThread, pyqtSignal
import subprocess

class ScraperThread(QThread):
    """
    Clase que maneja el hilo de scraping.
    """
    # Signal para señalizar que el hilo de scraping ha terminado
    scraping_finished = pyqtSignal()

    def __init__(self, search_item_encoded):
        """
        Inicializa el hilo de scraping.
        
        Args:
            search_item_encoded (str): El parámetro de búsqueda codificado.
        """
        super().__init__()
        self.search_item_encoded = search_item_encoded

    def run(self):
        """
        Ejecuta el hilo de scraping.
        """
        ml_command = f"scrapy crawl scrapper_ml -a search={self.search_item_encoded} -o items_ml.json"
        ebay_command = f"scrapy crawl scrapper_ebay -a search={self.search_item_encoded} -o items_ebay.json"

        try:
            subprocess.run(ml_command, shell=True, check=True)
            subprocess.run(ebay_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
        
        self.scraping_finished.emit()
