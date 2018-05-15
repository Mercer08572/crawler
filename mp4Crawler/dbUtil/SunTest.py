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

ts.bsTest(html_doc);

