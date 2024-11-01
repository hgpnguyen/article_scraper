# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    byline = scrapy.Field()
    updated_date = scrapy.Field()
