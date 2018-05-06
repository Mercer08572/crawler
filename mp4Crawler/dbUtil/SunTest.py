#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/5/2 15:50
# author : badbugu17
# file : TestSun
import configparser
import os

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



ts = SunTest();
ts.iniReader();
