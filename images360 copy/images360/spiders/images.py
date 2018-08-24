# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
from images360.items import ImageItem



class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15',
        'Host': 'image.so.com',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    def start_requests(self):

        base_url = 'http://image.so.com/j?'
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            print("正在爬取第 ",page," 页。")
            params = {
                'q': '现代沙发背景',
                'src': 'srp',
                'pn': 60,
                'ch': '',
                'sn': page * 60 + 50,
                'ran': 0,
                'ras': 0,
                'cn': 0,
                'gn': 0,
                'kn': 50,
            }

            url = base_url + urlencode(params)
            yield Request(url=url,callback=self.parse,headers=self.headers)

    def parse(self, response):
        result =json.loads(response.text)
        for image in result.get('list'):
            item=ImageItem()
            item['id']=image.get('id')
            item['url']=image.get('img')
            item['title']=image.get('title')
            item['thumb']=image.get('thumb')
            yield item
