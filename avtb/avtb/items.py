# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AvtbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    folder_name = scrapy.Field()
    #image = scrapy.Field()
    image_url = scrapy.Field()
    #player = scrapy.Field()
    player_url = scrapy.Field()
