'''
将爬取到的内容已HTML格式输出
'''
import time


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)


    def output_html(self):
        fileName = "../output/" + time.strftime("%Y-%m-%D") + "_output.html";
        fout = open(fileName, "w" , encoding="utf-8")

        fout.write('<html>')
        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
        fout.write("<body>")
        fout.write('<table style="border-collapse:collapse;" border="1">')

        #Python 默认编码为：ascii
        for data in self.datas:
            url = ""
            title = ""
            summary = ""
            try:
               url = data["url"]
               title = data["title"]
               summary = data["summary"]
            except RuntimeError as error:
                print("获取数据出现错误" + error)

            # print(url)
            # print(title)
            # print("================================================================================================================================================")
            # print(summary)

            fout.write("<tr>")
            fout.write("<td>%s</td>" % url)
            fout.write("<td>%s</td>" % title)
            fout.write("<td>%s</td>" % summary)
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()