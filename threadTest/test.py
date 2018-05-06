#!D:\Python\python.exe
#coding=utf-8
#文件名：test.py

import _thread
import time

# 为线程定义一个函数
def print_time(threadname,delay):
    count = 0;
    while count < 5:
        time.sleep(delay);
        count += 1;
        print("%s:%s" %(threadname,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))


try:
    _thread.start_new_thread(print_time,("thread1",2));
    _thread.start_new_thread(print_time,("thread2",4));
except Exception as e:
    print("ERROR:无法启动线程",e);

while 1:
    pass;
