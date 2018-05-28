#-*- coding:utf-8 -*-
# datatime : 2018/5/9 0:28
# author : badbugu17
# file : DBOperation.py
from mp4Crawler.dbUtil.MysqlDMLUtil import MysqlDMLUtil
from mp4Crawler.entity.CrawlStatus import CrawlStatus


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

    def addUsefulDataNew(self,usefulData,sqlList):
        """拼接批量插入SQL语句，将数据放入SQLlist中，批量处理。
        1、一个详情页面的信息放入一个sqlList中（目前版本）
        返回：返回加入数据的SQL列表"""

        usefulList = usefulData.urlEntity;  # 获取url列表

        mainInsertSql = " INSERT INTO PC_ResultData(id,years,name,memo,typeid) VALUES (%d,'%s','%s','%s',%d)" % (
            usefulData.id,usefulData.years,usefulData.name,usefulData.memo,usefulData.typeid);
        sqlList.append(mainInsertSql);

        for downloadUrl in usefulList:
            urlInsertSql = " INSERT INTO PC_ResultUrl(id,rdid,name1,name2,url) VALUES (%d,%d,'%s','%s','%s')" % (
                downloadUrl.id,downloadUrl.rdid,downloadUrl.name1,downloadUrl.name2,downloadUrl.url);
            sqlList.append(urlInsertSql);

        return sqlList;

    def querySql(self,sqlStr):
        return self._dbhepl.querySql(sqlStr);

    def getStatusById(self,id):
        """通过ID获取爬取状态表"""

        crawlStatus = CrawlStatus();

        getStatusSql = " SELECT id,startUrl,endUrl,step,memo,count,lastCount,pageSize,pageNum,updatePageNum FROM PC_Status WHERE id = %d" % (
            id);
        dataTup = self._dbhepl.querySql(getStatusSql);
        justOneStatus = dataTup[0];

        # 封装数据，有点傻
        crawlStatus.id = justOneStatus[0];
        crawlStatus.startUrl = justOneStatus[1];
        crawlStatus.endUrl = justOneStatus[2];
        crawlStatus.step = justOneStatus[3];
        crawlStatus.memo = justOneStatus[4];
        crawlStatus.count = justOneStatus[5];
        crawlStatus.lastCount = justOneStatus[6];
        crawlStatus.pageSize = justOneStatus[7];
        crawlStatus.pageNum = justOneStatus[8];
        crawlStatus.updatePageNum = justOneStatus[9];

        return crawlStatus;

    def updateStatusByStatus(self,crawlStatus):
        """根据status实体更新数据库中的status信息"""
        isOk = 0; # 0 失败  1 成功

        updateStatusSql = " UPDATE PC_Status SET startUrl = '%s',endUrl = '%s',step = %d,memo = '%d',count = %d,lastCount = %d,pageSize = %d,pageNum = %d,updatePageNum = %d WHERE id = %d" %(
                crawlStatus.startUrl,crawlStatus.endUrl,crawlStatus.step,crawlStatus.memo,crawlStatus.count,crawlStatus.lastCount,crawlStatus.pageSize,crawlStatus.pageNum,crawlStatus.updatePageNum,crawlStatus.id);
        isOk = self._dbhepl.execSql(updateStatusSql);

        return isOk;



