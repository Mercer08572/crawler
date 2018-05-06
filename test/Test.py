#coding=utf-8
import pymysql

connect = pymysql.Connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="ordermanager",
    charset="utf8"
)

cursor = connect.cursor();

sql = " select username,address from user ";

cursor.execute(sql);
abc = cursor.fetchall();
print(abc);
print(len(abc));
print(abc[0]);
print();
for row in abc:
    print(row);
    print("姓名：%s，地址：%s" % (row));

print("共查出：",cursor.rowcount,"条数据");

cursor.close();
connect.close();