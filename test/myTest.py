import urllib.request

def download():
    # response = urllib.request.urlopen("http://wx2.sinaimg.cn/mw600/56a2db55gy1fnfgm05k9gj20qn0qnjs8.jpg");
    # img = response.read();
    #
    # with open("../output/mzt.jpg", "wb") as f:
    #     f.write(img);

    # 此方法可以下载动态图片
    response = urllib.request.urlretrieve("http://wx2.sinaimg.cn/mw1024/0076BSS5ly1frqzyf68azg306t08ib29.gif","../output/mzdt.gif");
    print(response);
    print("写入成功")


def tessssst():
    sql = " SELECT column_name,is_nullable,data_type,column_key from information_schema.columns where table_schema = 'olddream' and table_name = 'typecho_users' ";
    print(sql);

download();