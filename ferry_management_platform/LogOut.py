# -*- coding: UTF-8 -*-
import logging
import logging.handlers
import os
import configparser


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


@singleton
class LogOutPut(object):
    def __init__(self):
        self.logger = logging.getLogger()  # 创建一个logger
        self.logger.setLevel(logging.DEBUG)  # Log等级总开关

        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关
        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        self.logger.addHandler(ch)

    def init_local_log(self, cfgpath, path, log_name):
        size = 100 * 1024 * 1024
        # 第二步，创建一个handler，用于写入日志文件
        if not os.path.exists(path):
            os.makedirs(path)
        config = configparser.ConfigParser()
        config.read(cfgpath)
        backupDays = 10
        loglevel = 'INFO'
        if config.has_option("LOG", "LogBackupDays"):
            backupDays = config.get("LOG", "LogBackupDays")
        if config.has_option("LOG", "LogLevel"):
            loglevel = config.get("LOG", "LogLevel")
        file_path = '%s%s' % (path, log_name)
        fh = logging.handlers.TimedRotatingFileHandler(file_path, when="D", interval=1, backupCount=int(backupDays), encoding='utf-8')
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

# singletonLog = LogOutPut()
