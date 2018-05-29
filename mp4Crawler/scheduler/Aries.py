#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/4/27 11:47
# author : badbugu17
# file : Aries
from mp4Crawler.entity.DownloadHtml import DownloadHtml
from mp4Crawler.scheduler.DBOperation import DBOperation
from mp4Crawler.scheduler.WebPageDownloader import WebPageDownloader
from mp4Crawler.scheduler.WebPageParser import WebPageParser


class Aries:
    """<白羊座>调度器"""
    dbo = DBOperation(); # 数据库操作类
    webPageDownloader = WebPageDownloader();  # 网页下载器
    webPageParser = WebPageParser(); # 网页解析器
    # step 1 解析status状态，之后的页面爬取都是从PC_Status表获取相关参数的
    new_url = "http://www.mp4ba.net/";
    indexHtmlDoc = webPageDownloader.htmlDownload(new_url);
    indexDownloadHtml = DownloadHtml();  # 下载后的页面实体
    indexDownloadHtml.url = new_url;
    indexDownloadHtml.htmlDoc = indexHtmlDoc;

    webPageParser.parserStatus(indexDownloadHtml)  # 初始化PC_Status表信息
    print("[<PC_Status>提示]：PC_Status表初始化成功")

    typeid = 5;  # 爬取的电影id    爬取不同类型的电影需要修改这里的属性
    # 1、国产电影 2、港台电影 3、欧美电影 4、日韩电影 5、海外电影 6、动画电影

    crawlStatus = dbo.getStatusById(typeid);  # 获取数据库中的爬取状态实体

    for i in range(crawlStatus.pageNum):
        # step 2 解析列表页，获取详细页的相关数据和URL放入数据库PC_WaitForCrawl表中
        startUrl = crawlStatus.endUrl;
        listHtmlDoc = webPageDownloader.htmlDownload(startUrl);
        listDownloadHtml = DownloadHtml(); # 列表页下载后页面实体
        listDownloadHtml.url = startUrl;
        listDownloadHtml.htmlDoc = listHtmlDoc;

        webPageParser.parserListPage(listDownloadHtml);

        # step 3 每次从PC_WaitForCrawl表中取出一条数据，进行下载解析，解析出详情页面的URL和相关信息











    # step 4 收尾工作，将PC_WaitForCrawl表中取出的并成功下载解析的记录删除，存入PC_CompleteCrawl表中

    # step 5 更新PC_Status表中的相关信息


