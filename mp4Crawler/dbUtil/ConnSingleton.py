#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/4/27 14:36
# author : badbugu17
# file : ConnSingleton
import configparser
import os
import pdb

import pymysql

from mp4Crawler.entity.ConnEntity import ConnEntity


class ConnSingleton:

    """数据库单例类
    获取数据库连接，游标。关闭数据库连接和游标（目前只针对mysql数据库进行操作）
    """

    _connection = None; # 连接对象
    _cursor = None; # 游标
    _singleton = None; # 单例创建标识

    _connEntity = ConnEntity();

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super(ConnSingleton,cls).__new__(cls);
        return cls._singleton;

    # def __init__(self):
    #     # 读取配置文件connectionInfo.ini
    #
    #     if self._connEntity.ip is not None:
    #         return;
    #
    #     connectInfo_path = os.path.abspath("..");
    #     connectInfo_path = os.path.join(connectInfo_path, "resources/connectionInfo.ini");
    #
    #     print("[临时<ConnSingleton.py>提示]：资源文件的路径为：", connectInfo_path);
    #
    #     config = configparser.ConfigParser();
    #     config.read(connectInfo_path);
    #
    #     # pdb.set_trace() # 命令行调试
    #
    #     self._connEntity.ip = config.get("mysqlDB", "ip");  # 获取数据库ip地址
    #     self._connEntity.port = config.get("mysqlDB", "port");  # 获取数据库
    #     self._connEntity.db = config.get("mysqlDB", "db");  # 获取数据库名称
    #     self._connEntity.user = config.get("mysqlDB", "user");  # 获取用户名
    #     self._connEntity.passwd = config.get("mysqlDB", "passwd");  # 获取密码
    #     self._connEntity.charset = config.get("mysqlDB", "charset");  # 获取编码


    def get_cursor(self):
        cursor = self._openConnect();
        return cursor;

    def _openConnect(self):
        """打开连接connection返回游标cursor"""

        if self._connection is not None:
            pass;
        else:
            self._connection = pymysql.Connect(
                # host = self._connEntity.ip,
                # port = int(self._connEntity.port),
                # user = self._connEntity.user,
                # passwd = self._connEntity.passwd,
                # db = self._connEntity.db,
                # charset = self._connEntity.charset
                host = "000.000.000.000",
                port = 0000,
                user = "000",
                passwd = "000",
                db = "000",
                charset = "utf_8"
            )

        self._cursor = self._connection.cursor();

        return self._cursor;

    def close_cursor(self):
        self._cursor.close();
        # self._connection.close();


