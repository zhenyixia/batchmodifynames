# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : log文件操作
# @Time  : 2021/10/17 9:40
# coding=utf-8

import logging
import logging.handlers

default_log_path = r'D:\all-dev-learning\008--python\programs\count\log\count.log'


class Logger:
    def __init__(self, log_path=default_log_path):
        # 创建一个logger实例
        self.logger = logging.getLogger("mylogger")
        self.logger.setLevel("DEBUG")  # 设置级别为DEBUG，覆盖掉默认级别WARNING
        # 创建一个handler,用于写入日志文件，handler可以把日志内容写到不同的地方
        fh = logging.FileHandler(log_path)
        fh.setLevel("INFO")
        # 再创建一个handler，用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel("INFO")
        # 定义handler的格式输出
        log_format = logging.Formatter("%(asctime)s [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s ")
        fh.setFormatter(log_format)  # setFormatter() selects a Formatter object for this handler to use
        ch.setFormatter(log_format)
        # 为logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger
