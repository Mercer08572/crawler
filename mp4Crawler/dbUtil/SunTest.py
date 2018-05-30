#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/5/2 15:50
# author : badbugu17
# file : TestSun
import configparser
import os
import urllib.parse

import time

from bs4 import BeautifulSoup

from mp4Crawler.entity.CrawlUrl import CrawlUrl
from mp4Crawler.entity.DownloadHtml import DownloadHtml
from mp4Crawler.scheduler.WebPageDownloader import WebPageDownloader
from mp4Crawler.scheduler.WebPageParser import WebPageParser


class SunTest:
    def iniReader(self):
        connectInfo_path = os.path.abspath("..");
        connectInfo_path = os.path.join(connectInfo_path, "resources/connectionInfo.ini");
        # print(connectInfo_path);
        config = configparser.ConfigParser();
        config.read(connectInfo_path);

        ip = config.get("mysqlDB", "ip");  # 获取数据库ip地址
        port = config.get("mysqlDB", "port");  # 获取数据库
        db = config.get("mysqlDB", "db");  # 获取数据库名称
        user = config.get("mysqlDB", "user");  # 获取用户名
        passwd = config.get("mysqlDB", "passwd");  # 获取密码
        charset = config.get("mysqlDB", "charset");  # 获取编码

        print(db);

    def joinurl(self):
        return urllib.parse.urljoin("http://www.baidu.com/qwer/asdf/","/abc/123/a.html");

    def dxFunction(self,dx):
        print(dx.id);
        print(dx.url);
        print(dx.createDate);
        print(dx.typeid);

    def bsTest(self,html_doc):
        soup = BeautifulSoup(html_doc);

        print("\n结构文档\n")
        print(soup.prettify());
        print();
        print("soup.title:",soup.title);
        print("soup.title.name:",soup.title.name);
        print("soup.title.string:",soup.title.string);
        print("soup.title.parent.name:",soup.title.parent.name);
        print("soup.p:",soup.p);
        print("soup.p[\"class\"]:",soup.p["class"]);
        print("soup.find_all(\"p\"):",soup.find_all("p"));
        print("soup.find(id=\"link3\"):",soup.find(id="link3"));
        print("soup.a[\"href\"]:",soup.a["href"]);

        print()
        print("循环")
        for link in soup.find_all("a"):
            print(link);

        print("\n新方法:")
        print(soup.find_all("a","sister"));

    def crawTest(self):
        html = WebPageDownloader();
        # parser = WebPageParser();
        htmlDoc = html.htmlDownload("http://www.mp4ba.net/") # 列表页
        # htmlDoc = html.htmlDownload("http://www.mp4ba.net/thread-5986-1-1.html") # 明细页
        # parser.parserListPage(htmlDoc);
        soup = BeautifulSoup(htmlDoc,"html.parser")
        # print(soup)
        # divtop = soup.find_all(id = "top");
        # for div in divtop:
            # previous = div.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling;  # name1
            # previous  = div.previous_sibling.previous_sibling.previous_sibling.previous_sibling; # name2
            # print(previous);
            # print(div.find("a").get("href"));

        spans = soup.find_all("span","xg1 num");
        for span in spans:
            # sps = span.previous_sibling;

            print(span);

            print(span.previous_sibling);
            spsa = span.parent;
            print(spsa);

            spsas = spsa.span;
            spsast = spsas.string;
            print(spsas);
            print(spsast[1:-1],"\n")

            # print(sps);
            # print(span,"\n");


    def sqlstest(self):
        insertSql = " INSERT INTO PC_WaitForCrawl(id,url,createDate,typeid,years,name,memo) values ('%s')" %(1);
        print(insertSql);


    def crawlTest(self,url):
        htmlDow = WebPageDownloader();
        htmlParser = WebPageParser();
        htmldoc = htmlDow.htmlDownload(url);
        downloadHtml = DownloadHtml();
        downloadHtml.url = url;
        downloadHtml.htmlDoc = htmldoc;
        htmlParser.parserListPage(downloadHtml);



ts = SunTest();
# url = ts.joinurl();
# print(url);
#
# print("\n参数类型为对象\n")
# dx = CrawlUrl();
# dx.id = 1;
# dx.url = "http://www.baidu.com";
# readtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# dx.createDate = readtime;
# dx.typeid = "1";
# ts.dxFunction(dx);


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# ts.bsTest(html_doc);

# ts.crawTest();

# ts.sqlstest();

# ts.crawlTest("http://www.mp4ba.net/forum-mp4ba-1-1.html");

webPageParser = WebPageParser();



# wait = webPageParser.parserInfo('<a href="http://www.mp4ba.net/thread-2421-1-14.html" onclick="atarget(this)" class="s xst">国产凌凌漆.From.Beijing.with.Love.1994.BD1080P.X264.AAC.Cantonese&amp;amp;Mandarin.CH</a>')
#
# print(wait);


html = WebPageDownloader();
htmlDoc = html.htmlDownload("http://www.mp4ba.net/") # 列表页
soup = BeautifulSoup(htmlDoc, "html.parser");
detailUrlList = soup.find_all("a","s xst");
for url in detailUrlList:
    wait = webPageParser.parserInfo(url);
    print(wait.name);
    print(wait.years);
    print(wait.memo);
    print()
