#-*- coding:utf-8 -*-
# datatime : 2018/5/9 0:28
# author : badbugu17
# file : DBOperation.py
from mp4Crawler.dbUtil.ConnSingleton import ConnSingleton
from mp4Crawler.dbUtil.MysqlDMLUtil import MysqlDMLUtil
from mp4Crawler.entity.CrawlStatus import CrawlStatus
from mp4Crawler.entity.CrawlUrl import CrawlUrl


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

    def addCompleteTableNew(self,crawlUrl,sqlList):
        # 拼接批量插入已爬表的SQL
        # insertSql = " INSERT INTO PC_CompleteCrawl(id,url,createDate,typeid,years,name,memo) values (%d,'%s','%s',%d,'%s','%s','%s')" % (
        #     index, crawlUrl.url, crawlUrl.createDate, crawlUrl.typeid, crawlUrl.years, crawlUrl.name, crawlUrl.memo);

        insertSql = " INSERT INTO PC_CompleteCrawl(id,url,createDate,typeid,years,name,memo) SELECT id,url,createDate,typeid,years,name,memo FROM PC_WaitForCrawl WHERE id = %d" % (crawlUrl.id);
        deleteSql = " DELETE FROM PC_WaitForCrawl WHERE id = %d" % (crawlUrl.id) ;

        sqlList.append(insertSql);
        sqlList.append(deleteSql);
        return sqlList;

    def getWaitByTopNum(self,size):
        """获取第一条待爬表实体"""
        cuList = [];  # 待爬实体列表
        findSql = " SELECT id,url,createDate,typeid,years,name,memo FROM PC_WaitForCrawl LIMIT 0,%d " % (size);
        dataTup = self._dbhepl.querySql(findSql);
        # data = dataTup[0];

        for data in dataTup:
            crawlUrl = CrawlUrl();
            # 封装
            crawlUrl.id = data[0];
            crawlUrl.url = data[1];
            crawlUrl.createDate = data[2];
            crawlUrl.typeid = data[3];
            crawlUrl.years = data[4];
            crawlUrl.name = data[5];
            crawlUrl.memo = data[6];
            # 加入list中
            cuList.append(crawlUrl);

        return cuList;

    def getWaitById(self,id):
        """根据ID获取待爬表实体"""
        crawlUrl = CrawlUrl();
        findSql = " SELECT id,url,createDate,typeid,years,name,memo FROM PC_WaitForCrawl WHERE id = %d " % (id);
        dataTup = self._dbhepl.querySql(findSql);
        data = dataTup[0];
        # 封装
        crawlUrl.id = data[0];
        crawlUrl.url = data[1];
        crawlUrl.createDate = data[2];
        crawlUrl.typeid = data[3];
        crawlUrl.years = data[4];
        crawlUrl.name = data[5];
        crawlUrl.memo = data[6];

        return crawlUrl;

    def deleteWaitFor(self,id):
        # 删除待爬表
        # dbhelp = MysqlDMLUtil();

        exeSql = " DELETE FROM PC_WaitForCrawl WHERE id = " + str(id);

        flag = self._dbhepl.execSql(exeSql);
        return flag;

    def getMaxPrimaryKeyValue(self,tablename):
        # 获取表主键最大值
        return self._dbhepl.getMaxPrimaryKeyValue(tablename);

    def batchExecSql(self,sqlList):
        # 批量执行SQL语句，插入数据库
        return self._dbhepl.batchExecSql(sqlList);

    # 临时，只针对www.mp4ba.net网站的爬取使用到
    def batchExecSqlJustForMp4ba(self,sqlList,waitCrawlUrlList):
        """同类型SQL连续超过3次执行，就需要使用此方法"""

        conn = ConnSingleton(); # 实例化连接类
        cursor = conn.get_cursor(); # 获取游标
        # 循环 执行SQL语句
        count = 0;  # 成功执行的SQL语句
        passCount = 0;  # 重复的SQL语句
        for index in range(len(sqlList)):
            try:
                isPass = self._checkDateBeforeAdd(waitCrawlUrlList[index],cursor);
                if isPass == 0:  # 0 不通过检查  1 通过检查
                    passCount += 1;
                    print("[<MysqlDMLUtil>提示]：第",index+1,"条记录重复，不做处理！");
                    continue;
                cursor.execute(sqlList[index]);
                count += 1; # 运行计数
            except Exception as e:
                print("[<MysqlDMLUtil>错误]:第",index+1,"条SQL语句：",sqlList[index],"插入数据库失败！\n",e);
                continue
        conn.close_cursor();

        return count, passCount;

    def _checkDateBeforeAdd(self,crawlUrl,cursor):
        # 检查数据，传递连接，不关闭

        isPass = 1;  # 0 不通过   1 通过

        waitCheckSqlStr = " SELECT COUNT(id) FROM PC_WaitForCrawl WHERE url = '%s' " % (crawlUrl.url);
        compCheckSqlStr = " SELECT COUNT(id) FROM PC_CompleteCrawl WHERE url = '%s' " % (crawlUrl.url);

        waitExistTup = self._dbhepl.querySqlWithoutOpenAndClost(waitCheckSqlStr,cursor);
        waitExist = waitExistTup[0][0];  # 如果大于0 说明已经在PC_WaitForCrawl表中已经存在 不需要再添加

        if waitExist > 0:
            isPass = 0;
        else:
            compExistTup = self._dbhepl.querySql(compCheckSqlStr);
            compExist = compExistTup[0][0];  # 如果大于0 说明PC_CompleteCrawl表中已经存在 不需要再添加
            if compExist > 0:
                isPass = 0;


        return isPass;

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

        updateStatusSql = " UPDATE PC_Status SET startUrl = '%s',endUrl = '%s',step = %d,memo = '%s',count = %d,lastCount = %d,pageSize = %d,pageNum = %d,updatePageNum = %d WHERE id = %d" %(
                crawlStatus.startUrl,crawlStatus.endUrl,crawlStatus.step,crawlStatus.memo,crawlStatus.count,crawlStatus.lastCount,crawlStatus.pageSize,crawlStatus.pageNum,crawlStatus.updatePageNum,crawlStatus.id);
        isOk = self._dbhepl.execSql(updateStatusSql);

        return isOk;



