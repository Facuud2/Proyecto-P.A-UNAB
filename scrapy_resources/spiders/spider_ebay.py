from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from ..items import ScrappercomparativeItem
from urllib.parse import quote_plus

class ScrapperSpiderEbay(CrawlSpider):
    """
    Spider para scrapear items de Ebay.
    """
    name = 'scrapper_ebay'
    item_count = 0
    allowed_domain = ['www.ebay.com']

    def __init__(self, search=None, *args, **kwargs):
        """
        Inicializa el spider con el parámetro de búsqueda.

        Args:
            search (str): El parametro de busqueda para ser codificado y usado en la URL.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super(ScrapperSpiderEbay, self).__init__(*args, **kwargs)
        search_encoded = quote_plus(search)
        self.start_urls = [f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw={search_encoded}&_sacat=0']

    rules = {
        # Links a los cuales debe acceder la spider
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//a[@class="s-item__link"]')),
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
        ebay_item = ScrappercomparativeItem()

        # Extraccion del nombre del item
        ebay_item['nombre'] = response.xpath('normalize-space(//h1)').extract()
        # Extraccion del precio del item
        ebay_item['precio'] = response.xpath('normalize-space(//div[@class="x-price-primary"]/span[@class="ux-textspans"])').extract()
        # Extraccion de si el envio es gratis
        ebay_item['envioGratis'] = response.xpath('normalize-space(//div[@class="ux-labels-values__values-content"])').extract()
        # Extraccion de la reputacion de la tienda
        ebay_item['reputacionTienda'] = response.xpath('//*[@id="mainContent"]/div[1]/div[2]/div/div/ul/li[1]/a/span/text()').extract()


        self.item_count += 1
        if self.item_count > 21:
            raise CloseSpider('item_exceeded')
        yield ebay_item