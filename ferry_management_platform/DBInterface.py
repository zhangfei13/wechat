#!/bin/python3
# #-*- coding: UTF-8 -*-

from OperateMySql import OperateMySql
from LogOut import LogOutPut


class DBInterface:
    def __init__(self):
        self._dbopr = None

    def init_db(self):
        self._dbopr = OperateMySql()
        if not self._dbopr.open_db():
            LogOutPut.error(msg='open database failed!')
            return False
        return True

    def vehicle_illegal_query(self, Socket):  # 车辆违法信息查询
        if self._dbopr is None:
            if not self.init_db():
                return False
        results = self._dbopr.getTaleInfo("vehicle_illegal_info", "vehicle_id", "illegal_type", "desc")

        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: HttpSever\r\n"
        response_body = str(results)

        response = response_start_line + response_headers + "\r\n" + response_body
        Socket.send(bytes(response, "utf-8"))

        return True

    def close_db(self):
        self._dbopr.close_db()
