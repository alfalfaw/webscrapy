# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field
#    user_item['id']=re.search('.*?id=(\d+)',response.xpath('//*[@id="tab-box"]').css('a').xpath('@href').extract_first(),re.S).group(1)
#         user_item['name']=response.xpath('//*[@id="j-name-wrap"]/span[1]/text()').extract()
#         user_item['description']=response.xpath('//*[@id="fan_count"]/text()').extract()
#         user_item['age']=response.xpath('//*[@id="age"]/span/text()').extract()
#         user_item['area']=response.xpath('//*[@id="head-box"]/dd/div[3]/span[1]/text()').extract()
#         user_item['follow_count']=response.xpath('//*[@id="follow_count"]/text()').extract()
#         user_item['fan_count']=response.xpath('//*[@id="fan_count"]/text()').extract()
#         user_item['events']=response.xpath('//*[@id="event_count"]/text()').extract()
#         user_item['level']=response.xpath('//*[@id="j-name-wrap"]/span[3]/text()').extract()
#         user_item['tag']=response.xpath('//*[@id="head-box"]/dd/div[1]/p/text()').extract()
#         user_item['counts']=response.xpath('//*[@id="rHeader"]/h4/text()').extract()
#         yield user_item

class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
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
