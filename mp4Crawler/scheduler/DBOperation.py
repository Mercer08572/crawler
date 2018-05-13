#-*- coding:utf-8 -*-
# datatime : 2018/5/9 0:28
# author : badbugu17
# file : DBOperation.py
from mp4Crawler.dbUtil.MysqlDMLUtil import MysqlDMLUtil


class DBOperation:

    def addWaitForTable(self,crawlUrl):
        dbhelp = MysqlDMLUtil();

        # 获取主键最大值
        maxPkValue = dbhelp.getMaxPrimaryKeyValue("PC_WaitForCrawl");

        insertSql = " INSERT INTO PC_WaitForCrawl(id,url,createDate,typeid) values ("+maxPkValue+",'"+crawlUrl.url+"','"+crawlUrl.createDate+"',"+crawlUrl.typeid+")";

        flag = dbhelp.execSql(insertSql);

        return flag;

    def addCompleteTable(self,crawlUrl):
        dbhelp = MysqlDMLUtil();

