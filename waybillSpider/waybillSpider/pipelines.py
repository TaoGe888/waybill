# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import json
import pymysql


class WaybillspiderPipeline(object):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
    conn.set_charset('utf8')

    def process_item(self, item, spider):
        cursor = self.conn.cursor()

        sql = r"insert into arrive_waybill(`id`,`company`,`num`,`num_date`,`num_time`,`user`,`user_cell`,`status`, `status_date`, `status_time`) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            item['id'],
            item['company'],
            item['num'],
            item['num_date'],
            item['num_time'],
            item['user'],
            item['user_cell'],
            item['status'],
            item['status_date'],
            item['status_time'],
        )

        effect_row = cursor.execute(sql)

        self.conn.commit()
        cursor.close()


# class WaybillspiderPipeline(object):
#     client = redis.StrictRedis('192.168.56.128', port=6379)
#
#     def process_item(self, item, spider):
#
#         find_id = self.client.get(item['id'])
#         if find_id:
#             return item
#         else:
#             json_str = json.dumps({
#                 'id': item['id'],
#                 'num': item['num'],
#                 'num_date': item['num_date'],
#                 'num_time': item['num_time'],
#                 'user': item['user'],
#                 'user_cell': item['user_cell'],
#                 'status': item['status'],
#                 'status_date': item['status_date'],
#                 'status_time': item['status_time'],
#             })
#             self.client.set(item['id'], json_str)

