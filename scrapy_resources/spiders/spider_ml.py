from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ScrappercomparativeItem
from scrapy.exceptions import CloseSpider

class ScrapperSpider(CrawlSpider):
    name = 'scrapper_ml'
    item_count = 0
    allowed_domain = ['www.mercadolibre.com.ar']

    def __init__(self, search=None, *args, **kwargs):
        super(ScrapperSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://listado.mercadolibre.com.ar/{search}#D[A:{search}]']

    rules = {

        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//li[contains(@class, "andes-pagination__button--next")]/a'))),
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//div[contains(@class, "ui-search-item__group--title")]/a[contains(@class, "ui-search-item__group__element")]')),
             callback='parse_item',
             follow=False),
    }

    def parse_item(self, response):
        ml_item = ScrappercomparativeItem()

        ml_item['nombre'] = response.xpath('normalize-space(//h1[@class="ui-pdp-title"]/text())').extract()
        ml_item['precio'] = response.xpath('normalize-space(//div[@class="ui-pdp-price__second-line"]/span/span/span[@class="andes-money-amount__fraction"]/text())').extract()
        ml_item['envioGratis'] = response.xpath('normalize-space(//div[@class="ui-pdp-media__body"]/p/span[@class="ui-pdp-color--GREEN ui-pdp-family--SEMIBOLD"]/text())').extract()
        ml_item['reputacionTienda'] = response.xpath('normalize-space(//div[@class="ui-review-capability__rating"]/div/p[contains(@class, "ui-review-capability__rating__average")])').extract()


        self.item_count += 1
        if self.item_count > 21:
            raise CloseSpider('item_exceeded')
        yield ml_item
