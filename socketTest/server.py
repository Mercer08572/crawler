#!D:\Python\python.exe
#coding=utf-8
#文件名：server.py

import socket

s = socket.socket();            # 创建socket对象
host = socket.gethostname();    # 设置本地主机名
port = 12345;                    # 设置端口
s.bind((host,port));              # 绑定端口

s.listen(5);                    # 等待客户端连接
while True:
    c,addr = s.accept();        # 建立客户连接
    print("连接地址:",addr);
    c.send("欢迎访问!".encode("utf-8"));
    c.close();                  # 关闭连接