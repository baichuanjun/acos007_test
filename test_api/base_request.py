# -*- coding:utf-8 -*-
import json

import requests

from config.config import REQUIRE
from config.config import HEADER
from logger import Log


class BaseRequest(object):

    def __init__(self, header={}):
        self.header = {**HEADER, **header}
        self.sum_url_count = 0
        self.request_url_count = 0
        self.succeed_url_count = 0
        self.error_url_count = 0
        self.other_error_url_count = 0
        self.business_error_url_count = 0

    def request(self, url, request_json):
        self.sum_url_count += 1
        request_data = requests.post(url=url, json={**request_json, **REQUIRE}, headers=self.header)
        self.request_url_count += 1
        if request_data.status_code == 200:
            json_data = json.loads(request_data.content)
            status = json_data.get("status") if json_data else False
            if status:
                self.succeed_url_count += 1
                print(
                    f"\033[1;32m succeed_status:{request_data.status_code}:请求成功succeed_url--->{url}请求参数:{request_json}\033[0m")
                """ 如果为True 就不需要处理了"""
                return
            else:
                self.business_error_url_count += 1
                print(
                    f"\033[1;31m error_status:{request_data.status_code}:详情见日志business. request_url--->{url}  请求参数{request_json}\033[0m")
                Log.business_error(json_data)
            """
            代表请求成功
            1.真实的请求成功。
            2.业务出问题了
            """
        else:
            self.other_error_url_count += 1
            print(
                f"\033[1;33m error_status:{request_data.status_code}详情见日志other. request_url--->{url}请求参数:{request_json}\033[0m")
            Log.other_error(request_data)
            """
            请求失败。所有的请求都需要记录下来
            """

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("XXX")


base_request = BaseRequest()
