import urllib

from bs4 import BeautifulSoup


def url_open(url):
    request = urllib.request.Request(url);
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0");
    response = urllib.request.urlopen(request);
    html = response.read();
    return html

def get_page(url):
    html = url_open(url);
    soup = BeautifulSoup(html,"html.parser");
    page_num = soup.find("span",class_="current-comment-page")