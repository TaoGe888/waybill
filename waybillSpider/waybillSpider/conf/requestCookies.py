# -*- coding:utf-8 -*-
__author__ = 'zqf'

cookies = {

}


cookies_str = ''

key_values = cookies_str.split('; ')
for key_value in key_values:
    key, value = key_value.split('=', maxsplit=1)
    cookies[key] = value
