'''
URL管理类
new_urls ：待爬URL集合
old_urls ：已爬URL集合
'''

class UrlManager(object):

    def __init__(self):#初始化两个集合
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, root_url):#添加单个的URL
        if root_url is None:
            return
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    def add_new_urls(self, new_urls):#添加多个URL集合
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):#待爬集合中是否还有URL
        return len(self.new_urls) != 0

    def get_new_url(self):#获取一个URL，并将它从待爬集合中去除，加入到已爬集合
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
