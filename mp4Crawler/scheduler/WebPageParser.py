#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/5/3 17:14
# author : badbugu17
# file : WebPageParser
from mp4Crawler.dbUtil.MysqlDMLUtil import MysqlDMLUtil


class WebPageParser:
    """网页解析器（解析出有用的url、网页信息）"""

    def parserListPage(self,htmlDoc):
        # 解析列表页数据，获取待爬页面
        if htmlDoc is None:
            return None;


