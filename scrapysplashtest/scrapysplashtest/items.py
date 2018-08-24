# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class UserItem(Item):
    id=Field()
    name=Field()
    description=Field()
    age=Field()
    area=Field()
    follow_count=Field()
    fan_count=Field()
    events=Field()
    level=Field()
    tag=Field()
    counts=Field()

class UserRelationItem(Item):
    id=Field()
    follows=Field()
    fans=Field()
