#!D:\Python\python.exe
#coding=utf-8
#文件名：sendTest.py

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "badbugu17@163.com";       # 发件人
receivers = "656105944@qq.com";   # 收件人

# 第三方 SMTP 服务
smtp_host = "smtp.163.com";
smtp_pass = "sll511";

content = """
    
""";
title = "人生苦短";


# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText(content,"plain","utf-8")
message["From"] = Header(sender,"utf-8");
message["To"] = Header(receivers,"utf-8");

message["Subject"] = Header(title,"utf-8");

try:
    smtpObj = smtplib.SMTP_SSL(smtp_host,465);
    smtpObj.login(sender,smtp_pass);
    smtpObj.sendmail(sender,[receivers,],message.as_string());
    print("邮件发送成功");
except Exception as e:
    print("ERROR：无法发送邮件",e);
