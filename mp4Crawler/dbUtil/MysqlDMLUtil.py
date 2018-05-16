#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/4/27 13:26
# author : badbugu17
# file : MysqlUtil
from mp4Crawler.dbUtil.ConnSingleton import ConnSingleton


class MysqlDMLUtil:
    """（增删改查）数据操纵语言DML"""

    def getMaxPrimaryKeyValue(self,tablename):
        # 获取最大的主键值

        conn = ConnSingleton();
        cursor = conn.get_cursor();

        primarykey = self._getTablePrimaryKey(tablename);

        sql = " SELECT MAX("+primarykey+") FROM "+tablename+" ";

        cursor.execute(sql);

        maxValue = cursor.fetchone();
        # print(maxValue);

        conn.close_cursor(); # 关闭连接

        if maxValue == (None,):
            return 1;
        else:
            maxValue = int(maxValue[0]);  # 转换为int类型
            maxValue += 1;  # 获取最大的主键值，可直接使用
            return maxValue;

    def querySql(self,sqlStr):
        # 执行SQL语句，返回json数据类型
        conn = ConnSingleton();
        cursor = conn.get_cursor();

        cursor.execute(sqlStr);
        dataTup = cursor.fetchall();

        # 关闭连接
        conn.close_cursor();

        return dataTup;

    def execSql(self,sqlStr):
        # 执行非查询语句
        flag = 1; # 1执行成功 2执行失败

        try:
            conn = ConnSingleton();
            cursor = conn.get_cursor();
            cursor.execute(sqlStr);
            conn.close_cursor(); # 关闭连接
        except Exception as exception:
            print(exception)
            flag = 0;

        return flag;

    def _getTablePrimaryKey(self,tablename):
        # 获取表的主键
        connsing =  ConnSingleton(); # 实例化数据库操作类
        cursor = connsing.get_cursor(); # 获取游标

        sql =  " SELECT column_name,is_nullable,data_type,column_key FROM information_schema.columns WHERE table_schema = \'bdm278066281_db\' AND table_name = \'"+tablename+"\' ";
        cursor.execute(sql);

        primarykey = "";
        for row in cursor.fetchall():
            column_key = row[3];
            if column_key == "PRI":
                primarykey = row[0];
                break;

        connsing.close_cursor();

        return primarykey





