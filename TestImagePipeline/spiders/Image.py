# -*- coding: utf-8 -*-
from scrapy.spider import  BaseSpider
from scrapy.selector import HtmlXPathSelector

from TestImagePipeline.items import TestimagepipelineItem


class ImageSpider(BaseSpider):
    name = "Image"
    allowed_domains = ["topit.me"]
    start_urls = ['http://www.topit.me/']

    def parse(self, response):
        # print response.text
        hxs = HtmlXPathSelector(response)
        imge  = hxs.select('//img/@src').extract()
        item = TestimagepipelineItem()
        item['image_urls'] = imge
        return item
        pass
