'''
网页下载器，使用urllib下载网页
直接使用最简单的方法下载网页
'''
import urllib.request

from bs4 import BeautifulSoup

from mp4Crawler.scheduler.WebPageDownloader import WebPageDownloader


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None

        response = urllib.request.urlopen(new_url)

        if response.getcode() != 200:
            return None

        return response.read().decode("utf-8");

    def download2(self, new_url):
        if new_url is None:
            return None

        response = urllib.request.urlopen(new_url)

        if response.getcode() != 200:
            return None

        return response.read();

abc = HtmlDownloader();
# respon = abc.download("http://www.baidu.com")
# print(respon);

# htmldoc = abc.download2("http://www.mp4ba.net/forum-mp4ba-1-1.html");
# soup = BeautifulSoup(htmldoc);
# print(soup.prettify());

abc = WebPageDownloader();
htmldoc2 = abc.htmlDownload("http://www.mp4ba.net/forum-mp4ba-1-1.html");
soup2 = BeautifulSoup(htmldoc2,"html.parser");
# print(soup2.prettify());
alist = soup2.find_all("a","s xst");
for x in alist:
    # print(x.get("href"));
    print(x.string)
print(len(alist));
