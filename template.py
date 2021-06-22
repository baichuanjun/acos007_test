# -*- coding:utf-8 -*-
import json

key_list = []


def get_key_list(dict_data):
    """
    获取所有的键值对
    :param dict_data:
    :return:
    """
    for k, y in dict_data.items():
        if isinstance(y, dict):
            get_key_list(y)
        else:
            if isinstance(y, int):
                key_list.append((k, "int"))
            elif isinstance(y, str):
                key_list.append((k, "string"))
            elif isinstance(y, list):
                if len(y)>0 and isinstance(y[0],dict):
                    for i in y:
                        get_key_list(i)
                else:
                    key_list.append((k, "list"))
            elif isinstance(y, tuple):
                key_list.append((k, "tuple"))
            elif isinstance(y, float):
                key_list.append((k, "float"))
            elif isinstance(y, bool):
                key_list.append((k, "bool"))
            else:
                key_list.append((k, type(y)))
    return key_list


with open("./template_data.json", "rb")as f:
    dict_data = f.read()
try:
    dict_data = json.loads(dict_data)
except:
    print("请输入一个dict")
key_list = []
type = input("请输入--->请求数据（1） 返回数据（2）：")
if type == "1":
    print("|参数名|必选|类型|说明|")
    print("|:----    |:---|:----- |-----   |")
    get_key_list_data =list(set( get_key_list(dict_data)))
    for k, y in get_key_list_data:
        print(f"| {k} | 是 | {y} | x |")
elif type == "2":
    print("|参数名|类型|说明|")
    print("|:----    |:----- |-----   |")
    get_key_list_data = get_key_list(dict_data)
    for k, y in get_key_list_data:
        print(f"| {k} | {y} | x |")
else:
    print("输入的参数有误。需要重新输入")


