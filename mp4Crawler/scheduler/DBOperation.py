#-*- coding:utf-8 -*-
# datatime : 2018/5/9 0:28
# author : badbugu17
# file : DBOperation.py
from mp4Crawler.dbUtil.MysqlDMLUtil import MysqlDMLUtil


class DBOperation:

    def addWaitForTable(self,new_url):
        dbhelp = MysqlDMLUtil();

        # PS：这里先使用querysql这个方法，以后会修改为别的方法操作插入语句

        # 获取主键最大值
        maxPkValue = dbhelp.getMaxPrimaryKeyValue("PC_WaitForCrawl");

        insertSql = " INSERT INTO PC_WaitForCrawl(id,url,createDate,typeid) values ("+maxPkValue+",'','',)"