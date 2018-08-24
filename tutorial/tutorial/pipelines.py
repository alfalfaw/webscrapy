# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TextPipeline(object):
    def __init__ (self):
        self.limit=50
    def process_item(self, item, spider):
        if item['text']:
#             评论长度大于50截取前50
            if len(item['text'])>self.limit:
                item['text']=item['text'][0:self.limit].rstrip()+'...'
            return item
        else:
                DropItem('Missing Text')
