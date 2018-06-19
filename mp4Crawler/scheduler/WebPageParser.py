#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/5/3 17:14
# author : badbugu17
# file : WebPageParser
import math
import time

import re
from bs4 import BeautifulSoup

from mp4Crawler.entity.CrawlStatus import CrawlStatus
from mp4Crawler.entity.CrawlUrl import CrawlUrl
from mp4Crawler.entity.DownloadUrl import DownloadUrl
from mp4Crawler.entity.UsefulData import UsefulData
from mp4Crawler.scheduler.DBOperation import DBOperation


class WebPageParser:
    """网页解析器（解析出有用的url、网页信息）"""

    def parserListPage(self,downloadHtml):

        dbo = DBOperation();
        downUrl = downloadHtml.url;  # 下载页面的url地址
        downHtml = downloadHtml.htmlDoc;  # 下载页面的HTMLDOC

        waitCrawlUrlList = []; # 为了减轻数据库负担，减少打开关闭连接的次数

        # 根据下载页面的URL地址可以获取电影类型 http://www.mp4ba.net/forum-mp4ba-2-1.html
        # typeid = downUrl[-8:-7];

        match = re.search("-\d-",downUrl);
        typeidOrig = match.group();
        typeid = typeidOrig[1:-1];

        typeid = int(typeid);

        # 解析列表页数据，获取待爬页面
        if downHtml is None:
            return None;

        soup = BeautifulSoup(downHtml,"html.parser");
        # 格式化HTML文档，并输出，方便调试使用
        # print(soup.prettify());

        # 获取页面上所有的电影连接
        detailUrlList = soup.find_all("a","s xst");

        sqlList = []; # 拼接的SQL集合
        index = dbo.getMaxPrimaryKeyValue("PC_WaitForCrawl"); # 获取主键最大值

        for tagA in detailUrlList:
            # 调用解析方法，解析出需要的数据
            wait = self.parserInfo(tagA);
            wait.typeid = typeid;

            dbo.addWaitForTableNew(wait, sqlList, index);
            waitCrawlUrlList.append(wait);
            index += 1;

        count, passCount = dbo.batchExecSqlJustForMp4ba(sqlList, waitCrawlUrlList); # 批量执行拼接的SQL语句
        # print("[<WebPageParser>提示]:批量SQL共", len(sqlList), "条，重复", passCount, "条，成功插入", count, "条!\n")
        return count, passCount, len(sqlList);


    def parserInfo(self,tagA):
        wait = CrawlUrl();
        original = tagA.string;

        # 解析出描述，“[]”中的内容
        leftIndex = original.find("[");
        rightIndex = original.find("]");
        memo = None;  # 描述
        if leftIndex != -1 and rightIndex != -1:
            rightIndex = rightIndex + 1;
            memo = original[leftIndex:rightIndex];
            # 去除 [] 获取文本内容
            memo = memo[1:-1];
        else:
            memo = "未知[见name]";


        # 原始信息去除 后面 [] 的信息
        original = original[0:leftIndex];

        # 解析出年份
        years = None;
        name = None;
        firstSpace = original.find(" ");
        if firstSpace == -1:  # 没有找到
            years = "未知[见name]";
            name = original;
        else:
            years = original[0:firstSpace];
            # 解析出标题
            nameIndex = firstSpace + 1;
            name = original[nameIndex:]




        # 解析出URL路径
        url = tagA.get("href");

        # 封装进 waitList 中
        wait.name = name.replace("'","");
        wait.years = years;
        wait.memo = memo.replace("'","");
        wait.url = url;

        # 临时赋值 ， 逻辑还没有想明白
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()); # 赋值创建时间
        # waitList.typeid = 1;
        wait.createDate = nowTime;

        return wait;

    def parserInfoPage(self,downloadHtml,crawlurl):
        """解析详细信息页面，获取真正实用信息
        :param downloadHtml 网页下载器下载的网页信息实体  内含 url 和 htmldoc 
        :param crawlurl 数据库中查询出的待爬数据
        """

        dbo = DBOperation() # 数据库操作类
        downUrl = downloadHtml.url;  # 下载页面的url地址
        downHtml = downloadHtml.htmlDoc;  # 下载页面的HTMLDOC

        usefulData = UsefulData();  # 解析出的数据储存实体
        urlList = []; # usefulData 中的urlEntity 集合

        index = dbo.getMaxPrimaryKeyValue("PC_ResultData");  # 返回主体表主键
        urlIndex = dbo.getMaxPrimaryKeyValue("PC_ResultUrl");  # 返回url数据表主键

        # 基础数据赋值
        usefulData.id = index;
        usefulData.typeid = crawlurl.typeid;
        usefulData.name = crawlurl.name;
        usefulData.years = crawlurl.years;
        usefulData.memo = crawlurl.memo;

        soup = BeautifulSoup(downHtml,"html.parser");  # 解析出页面的url，循环封装进主体信息中

        divTop = soup.find_all(id="top");
        for div in divTop:
            downloadUrl = DownloadUrl();  # URL储存实体

            magnetUrl = div.find("a").get("href");  # 磁力链接地址
            try:
                # name1 = div.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling;  # name1
                # name2  = div.previous_sibling.previous_sibling.previous_sibling; # name2
                name1 = div.find_previous_sibling("br").previous_sibling;
                name2 = name1.find_previous_sibling("br").previous_sibling;
            except Exception as e:
                name1 = div.a.previous_sibling;
                name2 = name1;

            if name1 is None:
                name1 = "名称1解析失败";
            if name2 is None:
                name2 = "名称2解析失败";

            if len(str(name1)) > 100:
                name1 = str(name1)[:100];

            if len(str(name2)) > 100:
                name2 = str(name2)[:100];

            # 填入数据
            downloadUrl.id = urlIndex;
            downloadUrl.rdid = usefulData.id;
            downloadUrl.name1 = str(name1);
            downloadUrl.name2 = str(name2);
            downloadUrl.url = str(magnetUrl);

            # 加入list中
            urlList.append(downloadUrl);

            # last setp urlIndex 自增
            urlIndex += 1;

        usefulData.urlEntity = urlList;

        sqlList = [];  # 拼出的批量SQL存放
        sqlList = dbo.addUsefulDataNew(usefulData,sqlList);

        # 批量执行SQL语句
        count = dbo.batchExecSql(sqlList);

        return count;

    def parserStatus(self,downloadHtml):
        """解析首页电影数
        1、国产电影 2、港台电影 3、欧美电影 4、日韩电影 5、海外电影 6、动画电影"""

        htmldoc = downloadHtml.htmlDoc;
        dbo = DBOperation();

        # typeDic = {}; 不再需要使用字典

        soup = BeautifulSoup(htmldoc,"html.parser");

        spans = soup.find_all("span", "xg1 num");

        for span in spans:
            # 获取电影类型
            typeName = span.previous_sibling;
            typeid = None;
            if typeName == "国产电影":
                typeid = 1;
            elif typeName == "港台电影":
                typeid = 2;
            elif typeName == "欧美电影":
                typeid = 3;
            elif typeName == "日韩电影":
                typeid = 4;
            elif typeName == "海外电影":
                typeid = 5;
            elif typeName == "动画电影":
                typeid = 6;

            # 获取电影数量
            moveSum__ = span.string;
            moveSum = moveSum__[1:-1];
            moveSum = int(moveSum);

            crawlStatus = dbo.getStatusById(typeid); # 获取数据库中的爬取状态实体

            # 将电影数加入字典中
            # typeDic[typeid] = moveSum;

            crawlStatus.typeid = typeid;
            crawlStatus.count = moveSum;

            # 计算网站最大页数 向上取整，不足1页按1页计算
            pageNum = math.ceil(crawlStatus.count / crawlStatus.pageSize);
            crawlStatus.pageNum = pageNum;

            # 获取需要更新的页数
            updatePageNum = math.ceil((crawlStatus.count - crawlStatus.lastCount) / crawlStatus.pageSize);
            crawlStatus.updatePageNum = updatePageNum;

            # 将这次查询到count赋值给lastcount
            crawlStatus.lastCount = moveSum;
            # 将count的值清零
            crawlStatus.count = 0;

            isOk = dbo.updateStatusByStatus(crawlStatus);

        return;



















