# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json


class ScrapperComparativePipeline:

    def open_spider(self, spider):
        self.file = open('items.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        try:
            item['nombre'] = item.get('nombre', '').strip()
            item['precio'] = item.get('precio', '').strip()
            item['envioGratis'] = item.get('envioGratis', '').strip()
            item['reputacionTienda'] = item.get('reputacionTienda', '404NF').strip()

            # Convert 'precio' to a float if possible
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
