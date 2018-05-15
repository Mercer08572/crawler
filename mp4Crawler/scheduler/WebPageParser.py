#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/5/3 17:14
# author : badbugu17
# file : WebPageParser
from bs4 import BeautifulSoup

from mp4Crawler.entity.CrawlUrl import CrawlUrl


class WebPageParser:
    """网页解析器（解析出有用的url、网页信息）"""

    def parserListPage(self,htmlDoc):
        # 解析列表页数据，获取待爬页面
        if htmlDoc is None:
            return None;

        soup = BeautifulSoup(htmlDoc);
        # 格式化HTML文档，并输出，方便调试使用
        # print(soup.prettify());

        # 获取页面上所有的电影连接
        detailUrlList = soup.find_all("a","s xst");

        for tagA in detailUrlList:
            waitList = CrawlUrl();
            original = tagA.string;





