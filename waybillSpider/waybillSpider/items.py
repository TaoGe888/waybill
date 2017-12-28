# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class WaybillspiderItem(scrapy.Item):
    id = Field()
    company = Field()
    num = Field()
    num_date = Field()
    num_time = Field()
    user = Field()
    user_cell = Field()
    status = Field()
    status_date = Field()
    status_time = Field()
