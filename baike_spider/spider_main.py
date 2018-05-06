from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()#url控制器
        self.downloader = html_downloader.HtmlDownloader()#网页下载器
        self.parser = html_parser.HtmlParser()#网页解析器
        self.outputer = html_outputer.HtmlOutputer()#将最后的结果变成HTML输出

    def craw(self,root_url):
        cont = 1#计数
        self.urls.add_new_url(root_url)#将初始URL加入待爬集合
        while self.urls.has_new_url():#循环获取要爬取的URL
            try:
                new_url = self.urls.get_new_url()
                print("当前爬取 %d : %s" %(cont , new_url))
                html_cont = self.downloader.download(new_url)#下载URL
                new_urls,new_data = self.parser.parser(new_url,html_cont)#解析URL，返回网页中的其他URL和数据
                self.urls.add_new_urls(new_urls)#将URL加入待爬URL
                self.outputer.collect_data(new_data)#将爬取的数据返回HTML输入类

                if cont == 100:#获取100条数据
                    break
                cont = cont + 1
            except RuntimeError as error:
                print("爬虫爬取失败" + error)

        self.outputer.output_html()#将内容以HTML格式输出


if __name__=="__main__":#主函数
    root_url = "http://baike.baidu.com/item/Python"#初始URL
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)