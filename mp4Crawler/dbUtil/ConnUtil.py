#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/4/27 17:30
# author : badbugu17
# file : ConnUtil
import configparser
import os

import pymysql


class ConnUtil:

    """数据库获取连接，关闭接连相关操作（目前只针对mysql数据）"""
    def _get_curson(self):

        # 读取配置文件connectionInfo.ini

        connectInfo_path = os.path.abspath("..");
        connectInfo_path = os.path.join(connectInfo_path,"resources/connectionInfo.ini");

        config = configparser.ConfigParser();
        config.read(connectInfo_path);

        ip = config.get("mysqlDB","ip"); # 获取数据库ip地址
        port = config.get("mysqlDB","port"); # 获取数据库
        db = config.get("mysqlDB","db"); # 获取数据库名称
        user = config.get("mysqlDB","user"); # 获取用户名
        passwd = config.get("mysqlDB","passwd"); # 获取密码
        charset = config.get("mysqlDB","charset"); # 获取编码

        connect = pymysql.Connect(
            host = ip,
            port = int(port),
            user = user,
            passwd = passwd,
            db = db,
            charset = charset
        )

        cursor = connect.cursor();

        return cursor;

