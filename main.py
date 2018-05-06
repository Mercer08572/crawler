#!D:\Python\python.exe
import os

def print8(*args):
    f = open(1,'w',encoding='utf-8',closefd=False);
    print(*args,file=f);
    f.flush();
    f.close();

print8("Content-type: text/html");
print8();
print8("<meta charset=\"utf-8\">");
print8("<b>环境变量</b><br>");
print8("<ul>");
for key in os.environ.keys():
    print8("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]));
print8("</ul>");