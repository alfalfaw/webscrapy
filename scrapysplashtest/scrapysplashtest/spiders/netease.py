# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from urllib.parse import quote
from scrapysplashtest.items import UserItem,UserRelationItem
from scrapy_splash import SplashRequest
import json
import re

script = """
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  return splash:html()
end
"""
    
class NeteaseSpider(Spider):
    name = 'netease'
    allowed_domains = ['music.163.com']
    user_url='https://music.163.com/#/user/home?id={id}'
    follow_url='https://music.163.com/#/user/follows?id={id}'
    fan_url='https://music.163.com/#/user/fans?id={id}'
    event_url='https://music.163.com/#/user/event?id={id}'
    start_users=['119231969']
    
    def start_requests(self):
        for id in self.start_users:
            yield SplashRequest('https://music.163.com/#/user/home?id=119231969',self.parse_user,endpoint='execute',args={'lua_source':script,'wait':7})
            

    def parse_user(self, response):
        print(response.text)
        user_item=UserItem()
#         user_item['id']=re.search('.*?id=(\d+)',response.xpath('//*[@id="tab-box"]').css('a').xpath('@href').extract_first(),re.S).group(1)
        user_item['name']=response.xpath('//*[@id="j-name-wrap"]').extract()
#         user_item['description']=response.xpath('//*[@id="fan_count"]/text()').extract()
#         user_item['age']=response.xpath('//*[@id="age"]/span/text()').extract()
#         user_item['area']=response.xpath('//*[@id="head-box"]/dd/div[3]/span[1]/text()').extract()
#         user_item['follow_count']=response.xpath('//*[@id="follow_count"]/text()').extract()
#         user_item['fan_count']=response.xpath('//*[@id="fan_count"]/text()').extract()
#         user_item['events']=response.xpath('//*[@id="event_count"]/text()').extract()
#         user_item['level']=response.xpath('//*[@id="j-name-wrap"]/span[3]/text()').extract()
#         user_item['tag']=response.xpath('//*[@id="head-box"]/dd/div[1]/p/text()').extract()
#         user_item['counts']=response.xpath('//*[@id="rHeader"]/h4/text()').extract()
        print('description',response.xpath('//*[@id="fan_count"]/text()').extract())
        yield user_item
        
#         id=re.search('.*?id=(\d+)',response.xpath('//*[@id="tab-box"]').css('a').xpath('@href').extract_first(),re.S).group(1)
#         yield Request(self.follow_url.format(id=id),callback=self.parse_follows,meta={'from':'follow','id':id})
#         yield Request(self.follow_url.format(id=id),callback=self.parse_fans,meta={'from':'fan','id':id})
#         yield Request(self.follow_url.format(id=id),callback=self.parse_events,meta={'from':'event'})
        
        
    def parse_follows(self,response):
#         ul的直接子节点
        follows=response.xpath('//*[@id="main-box"]/li')
        for follow in follows:
            id=re.search('id=(\d+)',follow.xpath('.//a[@class="ava f-pr"]/@href').extract_first(),re.S).group(1)
            yield Request(self.user_url.format(id=id),callback=self.parse_user,meta={'from':'user','id':id})
            
        id=response.meta.get('id')
#         关注列表
        user_relation_item=UserRelationItem()
        
        follows=[{'id':re.search('id=(\d+)',follow.xpath('.//a[@class="ava f-pr"]/@href').extract_first(),re.S).group(1),'name':follow.xpath('.//a[@class="ava f-pr"]/@title').extract_first()
           } for follow in follows]
        user_relation_item['id']=id
        user_relation_item['follows']=follows
        user_relation_item['fans']=[]
        yield user_relation_item
        
    def parse_fans(self,response):
        fans=response.xpath('//*[@id="main-box"]/li')
        for fan in fans:
            id=re.search('id=(\d+)',fan.xpath('.//a[@class="ava f-pr"]/@href').extract_first(),re.S).group(1)
            yield Request(self.user_url.format(id=id),callback=self.parse_user,meta={'from':'user','id':id})
            
        id=response.meta.get('id')
#         粉丝列表
        user_relation_item=UserRelationItem()
        
        fans=[{'id':re.search('id=(\d+)',follow.xpath('.//a[@class="ava f-pr"]/@href').extract_first(),re.S).group(1),'name':follow.xpath('.//a[@class="ava f-pr"]/@title').extract_first()
           } for fan in fans]
        user_relation_item['id']=id
        user_relation_item['follows']=[]
        user_relation_item['fans']=fans
        yield user_relation_item
        
        
        
        
        
        
        
            
        


