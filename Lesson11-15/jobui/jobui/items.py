# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobuiItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    position = scrapy.Field()
    address = scrapy.Field()
    detail = scrapy.Field()
