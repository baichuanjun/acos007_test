# -*- coding:utf-8 -*-
import re

from config.config import is_filter_delete
from config.request_data_config import RequestData as RequestData
from config.urls_config import Urls, NullClass
from test_api.base_request import base_request
from test_api.handle.handle_data import handle_data
from utils import get_url, GetAcos007Url


def make_test_request():
    """
    生成所有测试的url
    :return:
    """
    url_list = GetAcos007Url().get_acos007_url()  # 获取所有url list
    filter_url_list = filter_url(url_list)  # 过滤掉不需要处理的url  如过滤掉delete 的请求

    for i in filter_url_list:
        url = get_url(i)
        for data in handle_data(trim_url(i)):
            base_request.request(url=url, request_json=data)
    print(f"一共:{len(url_list)}个请求，测试了其中的{len(filter_url_list)}个接口,忽略了{len(url_list)-len(filter_url_list)}个delete接口") #


def filter_url(url_list):
    handle_url_list = []
    if is_filter_delete:
        """
        过滤掉 delete 请求
        """
        for i in url_list:
            if str(i).find("delete") == -1:
                handle_url_list.append(i)
    return handle_url_list


def trim_url(url):
    return str(url).split("/").pop()
