#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/4/27 14:36
# author : badbugu17
# file : ConnSingleton
import configparser
import os

import pymysql


class ConnSingleton:

    """数据库单例类
    获取数据库连接，游标。关闭数据库连接和游标（目前只针对mysql数据库进行操作）
    """

    _connection = None; # 连接对象
    _cursor = None; # 游标
    _singleton = None; # 单例创建标识

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super(ConnSingleton,cls).__new__(cls);
        return cls._singleton;


    def get_cursor(self):
        cursor = self._openConnect();
        return cursor;

    def _openConnect(self):
        """打开连接connection返回游标cursor"""
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

        self._connection = pymysql.Connect(
            host = ip,
            port = int(port),
            user = user,
            passwd = passwd,
            db = db,
            charset = charset
        )

        self._cursor = self._connection.cursor();

        return self._cursor;

    def close_cursor(self):
        self._cursor.close();
        self._connection.close();


