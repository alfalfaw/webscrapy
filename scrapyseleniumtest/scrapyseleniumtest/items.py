# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Field,Item
import scrapy
class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image=Field()
    price=Field()
    deal=Field()
    title=Field()
    shop=Field()
    location=Field()
