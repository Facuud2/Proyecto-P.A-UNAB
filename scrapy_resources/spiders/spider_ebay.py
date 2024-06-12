from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from ..items import ScrappercomparativeItem

class ScrapperSpiderEbay(CrawlSpider):
    name = 'scrapper_ebay'
    item_count = 0
    allowed_domain = ['www.ebay.com']
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_nkw=samsung&_sacat=0']

    rules = {

        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//div[@class="s-item__image"]/a')),
             callback='parse_item',
             follow=False),
    }

    def parse_item(self, response):
        ebay_item = ScrappercomparativeItem()

        ebay_item['nombre'] = response.xpath('normalize-space(/html/body/div[2]/main/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/div/div[1]/h1/span[1]/text()/text())').extract()
        ebay_item['precio'] = response.xpath('normalize-space(/html/body/div[2]/main/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/span/text())').extract()
        ebay_item['envioGratis'] = response.xpath('normalize-space(/html/body/div[2]/main/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/div/div[11]/div/div/div/div[1]/div/div/div[2]/div/div/span[1]/text())').extract()
        ebay_item['reputacionTienda'] = response.xpath('normalize-space(/html/body/div[2]/main/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/div/div[2]/div/div/ul/li[1]/a/span/text())').extract()


        self.item_count += 1
        if self.item_count > 21:
            raise CloseSpider('item_exceeded')
        yield ebay_item