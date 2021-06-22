# -*- coding: utf-8 -*-
import logging, time

# log_path�Ǵ����־��·��
import os

from flask import request

cur_path = os.path.dirname(os.path.realpath(__file__))
now_data = time.strftime('%Y_%m_%d')
log_path = os.path.join(os.path.dirname(cur_path), 'logs', now_data)
# ������������logs�ļ��У����Զ�����һ��
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Log(object):

    def __init__(self):
        self.business = os.path.join(log_path, '%s_business.log' % time.strftime('%Y_%m_%d'))
        self.business_logger = logging.getLogger()
        self.business_logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            f'[%(asctime)s-%(created)f]:- %(filename)s] - %(levelname)s: %(message)s')

        self.other = os.path.join(log_path, '%s_othe.log' % time.strftime('%Y_%m_%d'))
        self.other_logger = logging.getLogger()
        # self.other_logger.setLevel(logging.DEBUG)
        # self.formatter = logging.Formatter(
        #     f'[%(asctime)s-%(created)f]:- %(filename)s] - %(levelname)s: %(message)s')
        #
        self.test = os.path.join(log_path, '%s_test.log' % time.strftime('%Y_%m_%d'))
        self.test_logger = logging.getLogger()
        # self.test_logger.setLevel(logging.DEBUG)
        # self.formatter = logging.Formatter(
        #     f'[%(asctime)s-%(created)f]:- %(filename)s] - %(levelname)s: %(message)s')

    def __business_console(self, message):
        fh = logging.FileHandler(self.business, 'a', encoding='utf-8')  # �����python3��
        fh.setFormatter(self.formatter)
        self.business_logger.addHandler(fh)
        self.business_logger.exception(message)
        # self.business_logger.removeHandler(fh)
        fh.close()

    def __other_console(self, message):
        fh = logging.FileHandler(self.other, 'a', encoding='utf-8')  # �����python3��
        fh.setFormatter(self.formatter)
        self.business_logger.addHandler(fh)
        self.other_logger.exception(message)
        self.business_logger.removeHandler(fh)
        fh.close()

    def __test_console(self, message):
        fh = logging.FileHandler(self.test, 'a', encoding='utf-8')  # �����python3��
        fh.setFormatter(self.formatter)
        self.test_logger.addHandler(fh)
        self.test_logger.exception(message)
        self.test_logger.removeHandler(fh)
        fh.close()

    def business_error(self, message):
        self.__business_console(message)

    def other_error(self, message):
        self.__other_console(message)

    def test_error(self, message):
        self.__test_console(message)


Log = Log()
