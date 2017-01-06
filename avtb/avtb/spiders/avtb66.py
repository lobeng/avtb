# -*- coding: utf-8 -*-
import scrapy
from avtb.items import AvtbItem
from scrapy.loader import ItemLoader

class Avtb66Spider(scrapy.Spider):
    name = "avtb66"
    allowed_domains = ["www.avtb66.com"]
    start_urls = ['http://www.avtb66.com/recent/']

    def parse(self, response):
        yield self.parse_item(response)
        for u in response.xpath('//a[@class="prevnext" or @class="thumbnail"]/@href').extract():
            if not u:
                continue
            catch_page = response.urljoin(u)
            yield scrapy.Request(catch_page, callback=self.parse)
        

    def parse_item(self, response):
        '''item_one = ItemLoader(item=AvtbItem,response=response)
        item_one.add_xpath('folder_name', '//div[@id="video" and class="row"]/h1/text()')
        item_one.add_xpath('image_url', '//video[@player_html5_api]/source[@label="360p"]/@src')
        item_one.add_xpath('player_url', '//video[@player_html5_api]/@poster')
        return item_one.load_item()'''

        item_one = AvtbItem()
        item_one['folder_name'] = response.xpath('//div[@id="video" and @class="row"]/h1/text()').extract()
        item_one['image_url'] = response.xpath('//video[@class="video-js vjs-default-skin"]/source[@label="360p"]/@src').extract()
        item_one['player_url'] = response.xpath('//video[@class="video-js vjs-default-skin"]/@poster').extract()
        return item_one
