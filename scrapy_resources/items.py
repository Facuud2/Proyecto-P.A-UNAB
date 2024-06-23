import scrapy

class ScrappercomparativeItem(scrapy.Item):
    """
    El modelo para los items scrapeados.

    Atributos:
        nombre (str): Nombre del item.
        precio (str): Precio del item.
        envioGratis (str): Si el item es enviado gratis.
        reputacionTienda (str): La reputación de la tienda.
    """

    nombre = scrapy.Field()  # Nombre del item.
    precio = scrapy.Field()  # Precio del item.
    envioGratis = scrapy.Field()  # Si el item es enviado gratis.
    reputacionTienda = scrapy.Field()  # La reputación de la tienda.
