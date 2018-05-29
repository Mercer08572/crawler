#coding=utf-8
import pymysql

# connect = pymysql.Connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     passwd="root",
#     db="ordermanager",
#     charset="utf8"
# )

connect = pymysql.Connect(
    host="101.201.211.96",
    port=3306,
    user="bdm278066232",
    passwd="qqaazz888",
    db="bdm278066261_db",
    charset="utf_8"
)

cursor = connect.cursor();

# sql = " select username,address from user ";
sql = " SELECT url FROM PC_WaitForCrawl WHERE id = 0";

cursor.execute(sql);
tkp = cursor.fetchall();
print(tkp[0][0]);
# print(tkp);
# print(len(tkp));
# print(tkp[0]);
# print();
# for row in tkp:
#     print(row);
#     print("URL：%s，名称：%s" % (row));
#
# print("共查出：",cursor.rowcount,"条数据");

cursor.close();
connect.close();