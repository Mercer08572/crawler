#-*- coding:utf-8 -*-
# datatime : 2018/5/9 0:28
# author : badbugu17
# file : DBOperation.py
from mp4Crawler.dbUtil.MysqlDMLUtil import MysqlDMLUtil


class DBOperation:

    _dbhepl = MysqlDMLUtil();

    def addWaitForTable(self,crawlUrl):
        # 将数据添加到待爬表
        # dbhelp = MysqlDMLUtil();

        # 获取主键最大值
        maxPkValue = self._dbhepl.getMaxPrimaryKeyValue("PC_WaitForCrawl");

        insertSql = " INSERT INTO PC_WaitForCrawl(id,url,createDate,typeid,years,name,memo) values (%d,'%s','%s',%d,'%s','%s','%s')" % (
            maxPkValue,crawlUrl.url,crawlUrl.createDate,crawlUrl.typeid,crawlUrl.years,crawlUrl.name,crawlUrl.memo);


        print(insertSql);

        flag = self._dbhepl.execSql(insertSql);

        return flag;

    def addWaitForTableNew(self,crawlUrl,sqlList,index):
        # 拼接批量插入待爬表的SQL语句
        insertSql = " INSERT INTO PC_WaitForCrawl(id,url,createDate,typeid,years,name,memo) values (%d,'%s','%s',%d,'%s','%s','%s')" % (
            index, crawlUrl.url, crawlUrl.createDate, crawlUrl.typeid, crawlUrl.years, crawlUrl.name, crawlUrl.memo);
        sqlList.append(insertSql);
        return sqlList;


    def addCompleteTable(self,crawlUrl):
        # 将数据添加到已爬表
        # dbhelp = MysqlDMLUtil();

        # 获取主键最大值
        maxPkValue = self._dbhepl.getMaxPrimaryKeyValue("PC_CompleteCrawl");

        insertSql = " INSERT INTO PC_CompleteCrawl(id,url,createDate,typeid,years,name,memo) values (%d,'%s','%s',%d,'%s','%s','%s')" % (
            maxPkValue, crawlUrl.url, crawlUrl.createDate, crawlUrl.typeid, crawlUrl.years, crawlUrl.name, crawlUrl.memo);

        flag = self._dbhepl.execSql(insertSql);

        return flag;

    def addCompleteTableNew(self,crawlUrl,sqlList,index):
        # 拼接批量插入已爬表的SQL
        insertSql = " INSERT INTO PC_CompleteCrawl(id,url,createDate,typeid,years,name,memo) values (%d,'%s','%s',%d,'%s','%s','%s')" % (
            index, crawlUrl.url, crawlUrl.createDate, crawlUrl.typeid, crawlUrl.years, crawlUrl.name, crawlUrl.memo);
        sqlList.append(insertSql);
        return sqlList;

    def deleteWaitFor(self,id):
        # 删除待爬表
        # dbhelp = MysqlDMLUtil();

        exeSql = " DELETE FROM PC_WaitForCrawl WHERE id = " + id;

        flag = self._dbhepl.execSql(exeSql);
        return flag;

    def getMaxPrimaryKeyValue(self,tablename):
        # 获取表主键最大值
        return self._dbhepl.getMaxPrimaryKeyValue(tablename);

    def batchExecSql(self,sqlList):
        # 批量执行SQL语句，插入数据库
        return self._dbhepl.batchExecSql(sqlList);

    def checkDateBeforeAdd(self,crawlUrl):
        # 检查数据，
        return



