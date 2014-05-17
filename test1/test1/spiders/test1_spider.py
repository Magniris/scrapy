from scrapy.spider import Spider
from scrapy.selector import Selector

from test1.items import MultiPageItem

class MultiPageSpider(Spider):
    name = "multi"
    allowed_domains = ["NOTHING YET"]
    start_urls = [
        #URLS go here
        ""
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
	items = []
        for site in sites:
	    item = MultiPageItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
	    items.append(item)
        return items
