#!D:\Python\python.exe
#coding=utf-8
#filename=test2.py

import configparser
import os

# 获取文件的当前路径（绝对路径）
cur_path = os.path.dirname(os.path.realpath(__file__));

# 获取config.ini的路径
config_path=os.path.join(cur_path,"test2.ini");

conf = configparser.ConfigParser();
conf.read(config_path);

print("cur_path:",cur_path);
print("os.path.realpath(__file__):",os.path.realpath(__file__))
print("config_path:",config_path);


print();

ip0 = conf.get("game0","ip");
port0 = conf.get("game0","port");
type0 = conf.get("game0","type");

print("ip0:",ip0);
print("port0:",port0);
print("type0:",type0);
