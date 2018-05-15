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

        insertSql = " INSERT INTO PC_WaitForCrawl(id,url,createDate,typeid,years,name,memo) values ("+maxPkValue+",'"+crawlUrl.url+"','"+crawlUrl.createDate+"',"+crawlUrl.typeid+","+crawlUrl.years+","+crawlUrl.name+","+crawlUrl.memo+")";
        insert = " INSERT INTO PC_CompleteCrawl() "
        flag = dbhelp.execSql(insertSql);

        return flag;

    def addCompleteTable(self,crawlUrl):
        dbhelp = MysqlDMLUtil();

        # 获取主键最大值
        maxPkValue = dbhelp.getMaxPrimaryKeyValue("PC_CompleteCrawl");

        insertSql = " INSERT INTO PC_CompleteCrawl(id,url,createDate,typeid,years,name,memo) VALUES ("+maxPkValue+" , "+crawlUrl.url+","+crawlUrl.createDate+","+crawlUrl.typeid+","+crawlUrl.years+","+crawlUrl.name+","+crawlUrl.memo+") ";

        flag = dbhelp.execSql(insertSql);

        return flag;

    def deleteWaitFor(self,id):
        dbhelp = MysqlDMLUtil();

        exeSql = " DELETE FROM PC_WaitForCrawl WHERE id = " + id;

        flag = dbhelp.execSql(exeSql);
        return flag;



