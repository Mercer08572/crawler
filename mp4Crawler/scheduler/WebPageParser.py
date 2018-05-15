#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/5/3 17:14
# author : badbugu17
# file : WebPageParser
import time

from bs4 import BeautifulSoup

from mp4Crawler.entity.CrawlUrl import CrawlUrl
from mp4Crawler.scheduler.DBOperation import DBOperation


class WebPageParser:
    """网页解析器（解析出有用的url、网页信息）"""

    def parserListPage(self,htmlDoc):

        dbo = DBOperation()

        # 解析列表页数据，获取待爬页面
        if htmlDoc is None:
            return None;

        soup = BeautifulSoup(htmlDoc,"html.parser");
        # 格式化HTML文档，并输出，方便调试使用
        # print(soup.prettify());

        # 获取页面上所有的电影连接
        detailUrlList = soup.find_all("a","s xst");

        for tagA in detailUrlList:
            waitList = CrawlUrl();
            original = tagA.string;

            # 解析出描述，“[]”中的内容
            leftIndex = original.index("[");
            rightIndex = original.index("]");
            rightIndex = rightIndex + 1;
            memo = original[leftIndex:rightIndex];

            # 去除 [] 获取文本内容
            memo = memo[1:-1];

            # 原始信息去除 后面 [] 的信息
            original = original[0:leftIndex];

            # 解析出年份
            firstSpace = original.index(" ");
            years = original[0:firstSpace];

            # 解析出标题
            nameIndex = firstSpace + 1;
            name = original[nameIndex:]

            # 解析出URL路径
            url = tagA.get("href");

            # 封装进 waitList 中
            waitList.name = name;
            waitList.years = years;
            waitList.memo = memo;
            waitList.url = url;

            # 临时赋值 ， 逻辑还没有想明白
            waitList.typeid = 1;

            # 赋值创建时间
            nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());

            waitList.createDate = nowTime;


            result = dbo.addWaitForTable(waitList);

            if (result == 1):
                print("提示：《",name,"》的信息已存入数据库");
            else:
                print("错误：《",name,"》的信息存入数据库失败");
                break;






