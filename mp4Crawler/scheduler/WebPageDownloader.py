#!D:\Python\python.exe
#-*- coding:utf-8 -*-
# datatime : 2018/5/3 17:12
# author : badbugu17
# file : WebPageDownloader
import urllib.request


class WebPageDownloader:
    """网页下载器"""

    def htmlDownload(self,new_url):
        if new_url is not None:
            request = urllib.request.Request(new_url);
            # 伪装成Chrome浏览器
            request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36");
            request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8");
            # request.add_header("Accept-Encoding","gzip, deflate");
            request.add_header("Accept-Language","zh-CN,zh;q=0.9");
            request.add_header("Cache-Control","max-age=0");
            request.add_header("Connection","keep-alive");
            request.add_header("Host","www.mp4ba.net");
            request.add_header("Upgrade-Insecure-Requests","1");

            response = urllib.request.urlopen(request);
            if response.getcode() != 200:
                return None;
            return response.read();
        else:
            return None;