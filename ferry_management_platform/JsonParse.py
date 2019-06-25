#!/bin/python3
# #-*- coding: UTF-8 -*-

import json
import os
from LogOut import LogOutPut


class JsonParser(object):
    def __init__(self, path=None, file=None):
        self._path = path
        self._file = file

    def read_json_file(self):
        JsonDic = None
        f = None

        if self._path is None:
            LogOutPut.error(msg='error, there have no json file path given!')
            return None
        if self._file is None:
            LogOutPut.error(msg='error, there have no json file given!')
            return None
        if not os.path.exists(self._path + self._file):
            LogOutPut.error(msg="the json file [%s] not exsits!" % (self._path + self._file))
            return None
        try:
            f = open(self._path+self._file, "r", encoding='UTF-8')
            JsonDic = json.load(f)

        except Exception as e:
            LogOutPut.error(msg=e)
        finally:
            if f:
                f.close()

        return json.dumps(JsonDic, ensure_ascii=False)


