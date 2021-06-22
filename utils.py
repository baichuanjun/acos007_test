# -*- coding:utf-8 -*-
import os
import re

from config.config import HOST, URL_PREFIX, project_path
from logger import Log


def get_url(suffix):
    return HOST + "/" + URL_PREFIX + suffix


def try_exception(func):
    def inner_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            Log.test_error(str(e))
        return result

    return inner_func


project_name = ""


class GetAcos007Url(object):
    """
    这个类主要用于获取同级aos007下面的url

    """
    def __init__(self):
        self.project_name = ""
        self.url_file_list = []
        self.path_list = []

    def get_acos007_url(self):
        find_path = os.path.dirname(os.path.dirname(project_path))
        project_dir = self._find_project_dir(find_path)
        url_path_dir = os.path.join(project_dir, "backend", "acos_backend", "flask_app", "resource")
        self._get_path_url(url_path_dir)
        for path in self.url_file_list:
            self._read_file_find_url(path)
        return self.path_list

    def _find_project_dir(self, path):
        path_list = os.listdir(path)
        for i in path_list:
            if os.path.isdir(os.path.join(path, i)) and i == "acos007":
                self.project_name = os.path.join(path, i)
            elif os.path.isdir(os.path.join(path, i)):
                self.project_name = self._find_project_dir(os.path.join(path, i))
            else:
                pass

        return self.project_name

    def _get_path_url(self, url_path_dir):
        """
        一个个文件找。然后匹配出对应的路径
        :param url_path_dir:
        :return:
        """
        dir_list = os.listdir(url_path_dir)
        for i in dir_list:
            abs_path = os.path.join(url_path_dir, i)
            if os.path.isdir(abs_path):
                self._get_path_url(abs_path)
            else:
                self.url_file_list.append(abs_path)

    def _read_file_find_url(self, path):

        with open(path, mode="rb")as f:
            lines_data = f.readlines()
            for i in lines_data:
                if not isinstance(i, str):
                    try:

                        i = i.decode()
                    except:
                        continue
                path_suffix = self._re_match(i)
                if path_suffix:
                    self.path_list.append(path_suffix)

    def _re_match(self, data):
        pattern = re.compile(r"/.*[)]")
        match_data = pattern.findall(data)
        if len(match_data) > 1:
            raise ValueError(f"错误路由错误{data}")
        elif len(match_data) == 1:
            return str(match_data[0]).replace("')", "").replace('")', '').replace(')', '')
        else:
            return None
