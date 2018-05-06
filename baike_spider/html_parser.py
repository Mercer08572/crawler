'''
网页解析器，把已经下载好的网页解析出来
使用第三方插件：BeautifultSoup进行解析
'''
import re
from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,"html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):#获取爬取到的URL
        new_urls = set()
        #/item/%----8
        links = soup.find_all("a", href=re.compile(r"/item/%\w"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url,new_url)#获取到的URL是残缺的URL，需要进行补全
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):#获取爬取到的数据
        res_data = {}

        #url
        res_data["url"] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>正则表达式</h1>
        title_node = soup.find("dd" , class_="lemmaWgt-lemmaTitle-title").find("h1")#标题
        try:
            res_data["title"] = title_node.get_text()
            #print(title_node.get_text())
        except:
            print("title获取文本出现问题")
            res_data["title"] = ""

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div" , class_="lemma-summary")#内容
        try:
            res_data["summary"] = summary_node.get_text()
            #print(summary_node.get_text())
        except:
            print("summary获取文本出现问题")
            res_data["summary"] = ""

        return res_data

