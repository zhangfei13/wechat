# -*- coding: UTF-8 -*-
import logging
import logging.handlers
import os


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


@singleton
class log(object):
    def __init__(self):
        self.logger = logging.getLogger()  # 创建一个logger
        self.logger.setLevel(logging.DEBUG)  # Log等级总开关
        self.cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.init_local_log(self.cur_path + '/logs/', 'info.log')

    def init_local_log(self, path, log_name):
        size = 100 * 1024 * 1024
        # 第二步，创建一个handler，用于写入日志文件
        if not os.path.exists(path):
            os.makedirs(path)
        backupDays = 10
        loglevel = 'INFO'
        file_path = '%s%s' % (path, log_name)
        fh = logging.handlers.TimedRotatingFileHandler(file_path, when="D", interval=1, backupCount=int(backupDays))
        fh.suffix = "%Y-%m-%d_%H-%M.log"
        #fh = logging.handlers.RotatingFileHandler(file_path, mode='a', maxBytes=size, backupCount=10)
        fh.setLevel(loglevel)  # 输出到file的log等级的开关
        formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        print(msg)
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
