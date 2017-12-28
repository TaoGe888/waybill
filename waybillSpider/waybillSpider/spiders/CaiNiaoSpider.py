# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider
from scrapy.http import Request

from waybillSpider.conf import requestCookies
from waybillSpider.items import WaybillspiderItem


class CainiaospiderSpider(CrawlSpider):
    name = 'CaiNiaoSpider'
    allowed_domains = ['cainiaoyz.i56.taobao.com']
    start_urls = ['https://cainiaoyz.i56.taobao.com/poststation/billSearch.htm?mailNo=&mobilePhone=&orderSeq=&recName=&logisticsCompanyName=%E5%85%A8%E9%83%A8&logisticsCompanyId=&status=search%3A4&fromDate=2017-09-28&toDate=2017-12-27&orderSource=all&sendPackageHome=all&haveComment=all&bizType=&currentPage=']

    def start_requests(self):
        c = requestCookies.cookies

        for page in range(1, 334):

            url = self.start_urls[0] + str(page)
            yield Request(
                url=url,
                method='POST',
                callback=self.parse_content,
                cookies=c,
            )

    def parse_content(self, response):

        tr_doms = response.xpath('//div[@class="search-result"]/table[@class="order-table"]/tbody/tr')
        for tr_dom in tr_doms:
            item = WaybillspiderItem()

            # 运单号
            id_dom = tr_dom.xpath('td[@class="cell id"]/a/text()').extract()
            item['id'] = id_dom[0] if id_dom else ''

            # 物流公司
            company_dom = tr_dom.xpath('td[@class="cell id"]/text()').extract()
            item['company'] = company_dom[2].strip() if company_dom else ''

            # 提货码
            num_dom = tr_dom.xpath('td[@class="cell num"]/span[1]/text()').extract()
            item['num'] = num_dom[0] if num_dom else ''

            # 提货码日期
            num_date_dom = tr_dom.xpath('td[@class="cell num"]/span[2]/text()').extract()
            item['num_date'] = num_date_dom[0] if num_date_dom else ''

            # 提货码时间
            num_time_dom = tr_dom.xpath('td[@class="cell num"]/span[3]/text()').extract()
            item['num_time'] = num_time_dom[0] if num_time_dom else ''

            # 收件人
            user_dom = tr_dom.xpath('td[@class="cell user J_UserInfo"]/div/span[1]/@data').extract()
            item['user'] = user_dom[0] if user_dom else ''

            # 收件人电话
            user_cell_dom = tr_dom.xpath('td[@class="cell user J_UserInfo"]/div/span[2]/@data').extract()
            item['user_cell'] = user_cell_dom[0] if user_cell_dom else ''

            # 包裹状态
            status_dom = tr_dom.xpath('td[@class="cell status"]/text()').extract()
            item['status'] = status_dom[0].strip() if status_dom else ''
            item['status_date'] = status_dom[1].strip() if status_dom else ''
            item['status_time'] = status_dom[2].strip() if status_dom else ''

            yield item
