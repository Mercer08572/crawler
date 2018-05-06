'''
网页下载器，使用urllib下载网页
直接使用最简单的方法下载网页
'''
import urllib.request


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None

        response = urllib.request.urlopen(new_url)

        if response.getcode() != 200:
            return None

        return response.read()