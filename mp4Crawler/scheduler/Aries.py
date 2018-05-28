#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/4/27 11:47
# author : badbugu17
# file : Aries

class Aries:
    """<白羊座>调度器"""

    # step 1 解析status状态，之后的页面爬取都是从PC_Status表获取相关参数的

    # step 2 解析列表页，获取详细页的相关数据和URL放入数据库PC_WaitForCrawl表中

    # step 3 每次从PC_WaitForCrawl表中取出一条数据，进行下载解析，解析出详情页面的URL和相关信息

    # step 4 收尾工作，将PC_WaitForCrawl表中取出的并成功下载解析的记录删除，存入PC_CompleteCrawl表中

    # step 5 更新PC_Status表中的相关信息


