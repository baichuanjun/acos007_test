# -*- coding:utf-8 -*-
import os

REQUIRE = {
    "uid": "KXHtUxMQaIlPQnqNa3jT"
}

HEADER = {

}

URL_PREFIX = "api"

HOST = "http://127.0.0.1:5000"
# HOST = "http://127.0.0.1:500"


TEST_MODE = "part"  # 测试一共两种模式 ：全量测试(all)/非全量测试(part)，全量:一个接口会根据参数不同可能会发送多次请求。 非全量:一个接口只会请求一次,随机获取参数

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 该项目的路径

is_filter_delete = True  # 是否过滤掉delete 请求
