#!/bin/python3
# #-*- coding: UTF-8 -*-

"""解析excel文件"""

import xlrd
import os
import json
from LogOut import LogOutPut


class ExcelParser(object):
    def __init__(self, path=None, file=None, savefile=None):
        self._path = path
        self._file = file
        self._savefile = savefile

    # 解析execl文件到json文件
    def ParseExcel2File(self):
        if self._path is None:
            LogOutPut.error(msg="the excel path is given none!")
            return False
        if not str(self._path).endswith("/"):
            self._path = self._path + "/"
        if self._file is None:
            LogOutPut.error(msg="the excel filename is given none!")
            return False
        if self._savefile is None:
            LogOutPut.error(msg="the save file is given none!")
            return False
        if not os.path.exists(self._path + self._file):
            LogOutPut.error(msg="the excel file [%s] not exsits!" % self._path + self._file)
            return False
        # 获取excel文件
        data = xlrd.open_workbook(self._path + self._file, encoding_override='utf-8')
        # 获取一个excel有多少个sheet
        sheetNames = list(data.sheet_names())
        LogOutPut.debug(msg=sheetNames)
        # 写入目标文件位置
        with open(self._savefile, "r+") as f:
            read_data = f.read()
            f.seek(0)
            f.truncate()  # 清空文件
        alldata = {}
        result = []
        # 遍历sheet
        for name in sheetNames:
            # 获取sheet
            sheet = data.sheet_by_name(name)
            # 获取总行数
            nrows = sheet.nrows
            # 获取总列数
            ncols = sheet.ncols
            # 获取一行的数值
            sheetTitle = sheet.row_values(0)

            # 获取具体单元格的值
            for i in range(1, nrows):
                cell = {}
                cell["id"] = str(sheet.row_values(i)[0]).split(".0")[0]
                cell["question"] = str(sheet.row_values(i)[1]).split(".0")[0]
                cell["answer"] = str(sheet.row_values(i)[2]).split(".0")[0]
                cell["item1"] = str(sheet.row_values(i)[3]).split(".0")[0]
                cell["item2"] = str(sheet.row_values(i)[4]).split(".0")[0]
                cell["item3"] = str(sheet.row_values(i)[5]).split(".0")[0]
                cell["item4"] = str(sheet.row_values(i)[6]).split(".0")[0]
                cell["item5"] = str(sheet.row_values(i)[7]).split(".0")[0]
                cell["explains"] = str(sheet.row_values(i)[8]).split(".0")[0]
                cell["url"] = str(sheet.row_values(i)[9])
                result.append(cell)

        alldata["result"] = result
        jsonInfo = json.dumps(alldata)
        file = open(self._savefile, 'a+', encoding='utf-8')
        file.write(jsonInfo)
        file.close()

    # 解析execl文件到json字符串, 返回json字符串
    def ParseExcel2Json(self):
        if self._path is None:
            LogOutPut.error(msg="the excel path is given none!")
            return None
        if not str(self._path).endswith("/"):
            self._path = self._path + "/"
        if self._file is None:
            LogOutPut.error(msg="the excel filename is given none!")
            return None
        if not os.path.exists(self._path + self._file):
            LogOutPut.error(msg="the excel file [%s] not exsits!" % (self._path + self._file))
            return None
        # 获取excel文件
        data = xlrd.open_workbook(self._path + self._file, encoding_override='utf-8')
        # 获取一个excel有多少个sheet
        sheetNames = list(data.sheet_names())
        LogOutPut.debug(msg=sheetNames)

        alldata = {}
        result = []
        # 遍历sheet
        for name in sheetNames:
            # 获取sheet
            sheet = data.sheet_by_name(name)
            # 获取总行数
            nrows = sheet.nrows
            # 获取总列数
            ncols = sheet.ncols
            # 获取一行的数值
            sheetTitle = sheet.row_values(0)

            # 获取具体单元格的值
            for i in range(1, nrows):
                cell = {}
                cell["id"] = str(sheet.row_values(i)[0]).split(".0")[0]
                cell["question"] = str(sheet.row_values(i)[1]).split(".0")[0]
                cell["answer"] = str(sheet.row_values(i)[2]).split(".0")[0]
                cell["item1"] = str(sheet.row_values(i)[3]).split(".0")[0]
                cell["item2"] = str(sheet.row_values(i)[4]).split(".0")[0]
                cell["item3"] = str(sheet.row_values(i)[5]).split(".0")[0]
                cell["item4"] = str(sheet.row_values(i)[6]).split(".0")[0]
                cell["explains"] = str(sheet.row_values(i)[7]).split(".0")[0]
                surl = ("%s" % sheet.row_values(i)[8]).replace(r"\\\\", "\\")
                surl = surl.replace("\\/", "/")
                surl = surl.replace("\\", "/")
                cell["url"] = surl
                print(surl)
                result.append(cell)

        alldata["result"] = result

        return alldata

