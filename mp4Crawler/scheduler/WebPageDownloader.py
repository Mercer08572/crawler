#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/5/3 17:12
# author : badbugu17
# file : WebPageDownloader
import urllib


class WebPageDownloader:
    """网页下载器"""

    def htmlDownload(self,new_url):
        if new_url is not None:
            response = urllib.request.urlopen(new_url);
            if response.getcode() != 200:
                return None;
            return response.read();
        else:
            return None;