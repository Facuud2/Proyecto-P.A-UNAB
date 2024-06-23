from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ScrappercomparativeItem
from scrapy.exceptions import CloseSpider
from urllib.parse import quote_plus


class ScrapperSpider(CrawlSpider):
    """
    Spider para scrapear items de MercadoLibre.
    """
    name = 'scrapper_ml'
    item_count = 0
    allowed_domain = ['www.mercadolibre.com.ar']

    def __init__(self, search=None, *args, **kwargs):
        """
        Inicializa el spider con el parámetro de búsqueda.

        Args:
            search (str): El parametro de busqueda para ser codificado y usado en la URL.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super(ScrapperSpider, self).__init__(*args, **kwargs)
        search_encoded = quote_plus(search)
        self.start_urls = [f'https://listado.mercadolibre.com.ar/{search_encoded}#D[A:{search_encoded}]']

    rules = {
        # Links a los cuales debe acceder la spider
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//li[contains(@class, "andes-pagination__button--next")]/a'))),
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//div[contains(@class, "ui-search-item__group--title")]/a[contains(@class, "ui-search-item__group__element")]')),
             callback='parse_item',
             follow=False),
    }

    def parse_item(self, response):
        """
        Analiza la respuesta y extrae los datos.

        Args:
            response (scrapy.http.Response): El objeto de respuesta.

        Yields:
            ScrappercomparativeItem: La data scrapeada.
        """
        ml_item = ScrappercomparativeItem()

        # Extraccion del nombre del item
        ml_item['nombre'] = response.xpath('normalize-space(//h1[@class="ui-pdp-title"]/text())').extract()
        # Extraccion del precio del item
        ml_item['precio'] = response.xpath('normalize-space(//div[@class="ui-pdp-price__second-line"]/span/span/span[@class="andes-money-amount__fraction"]/text())').extract()
        # Extraccion de si el envio es gratis
        ml_item['envioGratis'] = response.xpath('normalize-space(//div[@class="ui-pdp-media__body"]/p/span[@class="ui-pdp-color--GREEN ui-pdp-family--SEMIBOLD"]/text())').extract()
        # Extraccion de la reputacion de la tienda
        ml_item['reputacionTienda'] = response.xpath('normalize-space(//div[@class="ui-review-capability__rating"]/div/p[contains(@class, "ui-review-capability__rating__average")])').extract()

        self.item_count += 1
        if self.item_count > 21:
            raise CloseSpider('item_exceeded')
        yield ml_item

