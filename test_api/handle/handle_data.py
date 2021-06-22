# -*- coding:utf-8 -*-
import config.raw_data_get as raw_request_data
from config.request_data_config import RequestData as RequestData
from config.config import TEST_MODE
import random


def handle_data(handle_data_name):
    """
    操作处理数据
    :param handle_data_name:
    :return:
    """

    if hasattr(raw_request_data, handle_data_name):
        raw_data = eval(f"raw_request_data.{handle_data_name}")
    else:
        raw_data = {}
    list_data = []
    if TEST_MODE == "part":
        list_data = [generate(raw_data)]
    elif TEST_MODE[:7] == "part":
        part = int(TEST_MODE[-1])
        for i in range(part):
            list_data.append(generate(raw_data))
    else:
        pass
    return list_data


def generate(data):
    """
    假定请求参数中 list 内部不会再有dict
    :param data:
    :return:
    """
    new_data = {}
    for k, y in data.items():
        if hasattr(RequestData, k):
            value = getattr(RequestData, k)
            new_data[k] = random.choice(value) if isinstance(value, list) else value
        elif isinstance(y, dict):
            # 说明有下一层
            new_data[k] = generate(data[k])

        else:
            new_data[k] = None
            # 说明有下一层

    return new_data
