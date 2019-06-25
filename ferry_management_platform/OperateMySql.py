#!/usr/local/bin/python3.6
import pymysql
import threading
import os
from LogOut import LogOutPut
from managePlatform import settings


class OperateMySql:
    def __init__(self):
        self._mutex = threading.Lock()
        self._conn = None
        self._db_host = settings.DATABASES.get('default').get('HOST')
        self._db_name = settings.DATABASES.get('default').get('NAME')
        self._username = settings.DATABASES.get('default').get('USER')
        self._password = settings.DATABASES.get('default').get('PASSWORD')

    def open_db(self):
        if self._conn is None:
            try:
                self._conn = pymysql.connect(self._db_host, self._username, self._password, self._db_name)
            except pymysql.Error as e:
                LogOutPut.error(msg="exit, Opened database fail: host:%s, dbname:%s, username:%s  %s" % (self._db_host, self._db_name, self._username, e))
                return False
            return True
        return True

    def close_db(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def getTaleInfo(self, table, *iterable):
        argvs = iterable
        subSql = ''
        retDic = []
        for i in range(0, len(argvs)):
                subSql = subSql + '`' + argvs[i] + '`'
                if i + 1 < len(argvs):
                        subSql = subSql + ', '
        strSqlCmd = "SELECT  " + subSql + " from " + table
        print(strSqlCmd)
        self._mutex.acquire()
        if self._conn is None:
            if self.open_db() is False:
                self._mutex.release()
                return False
        cur = self._conn.cursor()
        cur.execute(strSqlCmd)
        rows = cur.fetchall()

        for row in rows:
            retData = {}
            for i in range(0, len(argvs)):
                retData.setdefault(argvs[i], (str(row[i])))
            retDic.append(retData)
        cur.close()
        self._mutex.release()
        print(retDic)
        return retDic

    def execute_sql(self, sql, is_lock=True, is_close=False):
        if self._conn is None:
            if self.open_db() is False:
                return False

        # 加锁
        if is_lock:
            self._mutex.acquire()
        try:
            result = self._conn.cursor().execute(sql)
            self._conn.commit()
        except pymysql.Error as e:
            LogOutPut.error(msg="Execute Sql Fail: %s %s" % (sql, e))
            result = False

        if is_close:
            self.close_db()

        # 解锁
        if is_lock:
            self._mutex.release()
        return result

