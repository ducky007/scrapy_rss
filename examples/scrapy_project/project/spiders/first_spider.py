# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from project.items import ShopItem


class ShopSpider(CrawlSpider):
    name = 'first_spider'
    allowed_domains = ['woxcab.github.io']
    start_urls = ['https://woxcab.github.io/scrapy_rss/']

    rules = (
        Rule(LinkExtractor(allow=(r'item\d+\.html$',)),
             callback='parse_item'),
        Rule(LinkExtractor()),
    )

    def parse_item(self, response):
        item = ShopItem()
        item['name'] = response.css('h4 a ::text').extract_first()
        item['price'] = response.css('h4.pull-right ::text').extract_first()
        item.rss.description = ' '.join(p.strip() for p in response.css('.caption-full p ::text').extract())
        item['rating'] = response.css('.ratings p:nth-child(2) ::text').extract()[-1].strip()
        item['reviews'] = response.css('.ratings p:nth-child(1) ::text').extract_first()
        item['review_dates'] = response.css('.col-md-12 span ::text').extract()
        item.rss.author = 'Shop'
        item.rss.guid.isPermaLink = True
        item.rss.guid = response.url
        item.rss.link = item.rss.comments = response.url
        item.rss.category = response.css('.list-group-item .active ::text')
        item.rss.enclosure = {'type': 'image/png',
                              'url': response.xpath('//div[@class="thumbnail"]/img/@src').extract_first(),
                              'length': 0}
        yield item


