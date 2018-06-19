#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/4/27 11:47
# author : badbugu17
# file : Aries
import getopt
import time

import sys

from mp4Crawler.entity.DownloadHtml import DownloadHtml
from mp4Crawler.scheduler.DBOperation import DBOperation
from mp4Crawler.scheduler.WebPageDownloader import WebPageDownloader
from mp4Crawler.scheduler.WebPageParser import WebPageParser


class Aries:

    _dbo = DBOperation(); # 数据库操作类
    _webPageDownloader = WebPageDownloader();  # 网页下载器
    _webPageParser = WebPageParser(); # 网页解析器

    def mainFunction(self):

        """<白羊座>调度器"""

        # 方法调用，使用linux脚本定时执行
        # 格式 python Aries.py -ild -t
        try:
            opts, args = getopt.getopt(sys.argv[1:],"ildt:", ["init", "list", "detail", "type="]);

            if len(opts) == 0 :
                print("[<Aries.py>错误]：请输入参数\n");
                return;


            typeid = 0;  # 爬取的电影id    爬取不同类型的电影需要修改这里的属性         PS:注意
            # 1、国产电影 2、港台电影 3、欧美电影 4、日韩电影 5、海外电影 6、动画电影
            crawlStatus = None;
            startUrl = None;
            for name, value in opts:
                if value != "":
                    typeid = int(value);
                    crawlStatus = self._dbo.getStatusById(typeid);
                    startUrl = crawlStatus.endUrl;
                    break;

            moveTypeName = "";
            if typeid == 1:
                moveTypeName = "国产电影";
            elif typeid == 2:
                moveTypeName = "港台电影";
            elif typeid == 3:
                moveTypeName = "欧美电影";
            elif typeid == 4:
                moveTypeName = "日韩电影";
            elif typeid == 5:
                moveTypeName = "海外电影";
            elif typeid == 6:
                moveTypeName = "动画电影";

            nowDateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("[!!!]开始时间：", nowDateTime)
            print("目前爬取的电影类型为：", moveTypeName, "\n");

            # typeid = 5;  # 爬取的电影id    爬取不同类型的电影需要修改这里的属性         PS:注意
            # # 1、国产电影 2、港台电影 3、欧美电影 4、日韩电影 5、海外电影 6、动画电影
            #
            # crawlStatus = self._dbo.getStatusById(typeid);  # 获取数据库中的爬取状态实体
            # startUrl = crawlStatus.endUrl;

            for opt in opts:
                if "-i" in opt:
                    # 进行初始化操作
                    print("[<Aries.py>提示]：进行初始化PC_Status表\n");

                    # step 1 解析status状态，之后的页面爬取都是从PC_Status表获取相关参数的
                    self.initStatus();

                    break;
                if "-l" in opt:
                    # 进行列表页的解析
                    print("[<Aries.py>提示]：进行列表页的解析\n");
                    # step 2 解析列表页
                    self.listInfoParser(crawlStatus);

                    break;
                if "-d" in opt:
                    # 进行详情页的解析
                    print("[<Aries.py>提示]：进行详情页的解析\n");
                    # step 3 每次从PC_WaitForCrawl表中取出一条数据，进行下载解析，解析出详情页面的URL和相关信息
                    # crawlUrl = dbo.getWaitByTop1();
                    self.detailInfoParser(crawlStatus);  # step3 step4 在方法内执行

                    break;

        except getopt.GetoptError as ge:
            print("[<Aries.py>错误]：输入的参数有误，请重新数据!\n");
            # raise ge;
        nowDateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
        print("[!!!]结束时间：", nowDateTime, "\n");


    def initStatus(self):

        startTime = time.time();

        """初始化status表，逻辑还欠考虑"""
        new_url = "http://www.mp4ba.net/";
        indexHtmlDoc = self._webPageDownloader.htmlDownload(new_url);
        indexDownloadHtml = DownloadHtml();  # 下载后的页面实体
        indexDownloadHtml.url = new_url;
        indexDownloadHtml.htmlDoc = indexHtmlDoc;

        self._webPageParser.parserStatus(indexDownloadHtml)  # 初始化PC_Status表信息

        endTime = time.time();
        diffTime = endTime - startTime;

        print("[<PC_Status>提示]：PC_Status表初始化成功!耗时%.2f秒\n" % (diffTime));

        return;

    def listInfoParser(self,crawlStatus):

        listPageRowCount = 0;  # 爬取的列表页电影数
        insertToTableCount = 0;  # 实际插入数据库中的列表页记录数
        repeatCount = 0;  # 重复的列表页记录数

        startTime = time.time();  # 获取开始时间

        startUrl = crawlStatus.endUrl; # 获取开始爬取的路径

        for i in range(crawlStatus.step):
            # step 2 解析列表页，获取详细页的相关数据和URL放入数据库PC_WaitForCrawl表中

            # pageNumber = startUrl[-6:-5]; # pageNumber修改取值方式
            pointIndex = startUrl.rfind(".");
            lastIndex = startUrl.rfind("-");
            pageNumber = startUrl[lastIndex+1:pointIndex];

            pageNumber = int(pageNumber);
            if pageNumber > crawlStatus.pageNum:
                print("[<Aries.py提示>]:该类型的电影已经爬取完毕！")
                break;

            # startUrl = crawlStatus.endUrl;
            listHtmlDoc = self._webPageDownloader.htmlDownload(startUrl);
            listDownloadHtml = DownloadHtml();  # 列表页下载后页面实体
            listDownloadHtml.url = startUrl;
            listDownloadHtml.htmlDoc = listHtmlDoc;

            succCount, passCount, sumCount = self._webPageParser.parserListPage(listDownloadHtml);
            insertToTableCount += succCount;
            repeatCount += passCount;
            listPageRowCount += sumCount;

            # startUrl = startUrl[:-6] + str(pageNumber + 1) + startUrl[-5:];
            startUrl = startUrl[:lastIndex+1] + str(pageNumber + 1) + startUrl[pointIndex:];

            print("[<Aries.py>提示]:第%d次循环结束，共解析出%d条列表页数据，成功插入%d条，重复%d条！" % (i+1,sumCount,succCount,passCount));

        # step 5 更新PC_Status表中的相关信息
        crawlStatus.endUrl = startUrl;
        self._dbo.updateStatusByStatus(crawlStatus);

        stopTime = time.time();
        diffTime = stopTime - startTime;

        print("┌-----------列表页爬取成功-------------");
        print("│               状态报告              ");
        print("│       总记录数：%d条                  " % (listPageRowCount));
        print("│       成功：%d条                      " % (insertToTableCount));
        print("│       重复：%d条                      " % (repeatCount));
        print("│       耗时：%.2f秒                    " % (diffTime));
        print("└-------------------------------------\n");

        return;

    def detailInfoParser(self,crawlStatus):
        loopNum = 5;

        infoCountSum = 0;  # 详情页解析数

        startTime = time.time();

        # 添加的已爬列表的SQL集合
        insertToCompSqlList = [];


        for i in range(loopNum):
            # cuList = self._dbo.getWaitByTopNum(crawlStatus.step);
            cuList = self._dbo.getWaitByTopNum(5);
            if len(cuList) != 0:
                for crawlUrl in cuList:
                    infoPageHtmlDoc = self._webPageDownloader.htmlDownload(crawlUrl.url);
                    infoDownloadHtml = DownloadHtml();  # 下载后的详情页实体
                    infoDownloadHtml.url = crawlUrl.url;
                    infoDownloadHtml.htmlDoc = infoPageHtmlDoc;

                    # 解析详情页面，并把数据保存到数据库中
                    infoCount = self._webPageParser.parserInfoPage(infoDownloadHtml, crawlUrl);
                    infoCountSum += infoCount;

                    # step 4 收尾工作，将PC_WaitForCrawl表中取出的并成功下载解析的记录删除，存入PC_CompleteCrawl表中
                    self._dbo.addCompleteTableNew(crawlUrl, insertToCompSqlList);  # 方法中已经加入了删除PC_WaitForCrawl表数据的SQL
                    # self._dbo.deleteWaitFor(crawlUrl.id);

                    # print("本次循环成功解析%d条记录\n" % (infoCount));
                connt = self._dbo.batchExecSql(insertToCompSqlList);
                print("%d条数据已从PC_WaitForCrawl表插入到PC_CompleteCrawl表中,PC_WaitForCrawl表数据已删除" % (connt / 2) )


            else:
                print("[<Aries.py>提示]:PC_WaitForCrawl表已爬空\n");
                break;


        endTime = time.time();
        diffTime = endTime - startTime;

        print("┌-----------详情页爬取成功-------------");
        print("│               状态报告              ");
        print("│        总记录数：%d条                  " % (infoCountSum));
        print("│        耗时：%.2f秒                  " % (diffTime));
        print("└-------------------------------------\n");

        return;

aries = Aries();
# aries.initStatus();
crawlStatus = aries._dbo.getStatusById(1);
# aries.listInfoParser(crawlStatus);

aries.detailInfoParser(crawlStatus);

# for i in range(6):
    # aries.initStatus();




