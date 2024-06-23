import json

class ScrapperComparativePipeline:
    """
    Pipeline para guardar los items scrapeados en JSON.

    Este pipeline guarda los items scrapeados en archivos JSON en función del nombre del spider.
    El nombre de la spider debe ser 'scrapper_ml' o 'scrapper_ebay'.
    Items con campos faltantes o invalidos se omiten.
    """

    def open_spider(self, spider):
        """
        Abre el archivo para escribir cuando el spider inicia.

        Args:
            spider (Spider): El spider que inicia
        """
        if spider.name == 'scrapper_ml':
            self.file = open('items_ml.json', 'w', encoding='utf-8')
        elif spider.name == 'scrapper_ebay':
            self.file = open('items_ebay.json', 'w', encoding='utf-8')
        else:
            self.file = open('error', 'w', encoding='utf-8')


    def close_spider(self, spider):
        """
        Cierra el archivo cuando el spider termina.

        Args:
            spider (Spider): El spider que termina.
        """
        self.file.close()


    def process_item(self, item, spider):
        """
        Procesa el item y lo escribe en el archivo.

        Args:
            item (dict): El item scrapeado.
            spider (Spider): El spider que scrapeo el item.

        Returns:
            dict: El item scrapeado.
        """
        try:
            item['nombre'] = item.get('nombre', '').strip()
            item['precio'] = item.get('precio', '').strip()
            item['envioGratis'] = item.get('envioGratis', '').strip()
            item['reputacionTienda'] = item.get('reputacionTienda', '404NF').strip()

            # Convierte 'precio' en float si es posible
            if item['precio']:
                try:
                    item['precio'] = float(item['precio'].replace(',', ''))
                except ValueError:
                    spider.logger.error(f"Unable to convert price: {item['precio']}")

            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
        except Exception as e:
            spider.logger.error(f"Error processing item: {e}")

        return item

