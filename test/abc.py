#coding=utf-8
import re

print(re.match("www","www.baidu.com").span())
print(re.match("com","www.baidu.com"))

line = "Cats are smarter than dogs";

matchObj = re.search(r"(.*) are (.*?) .*",line,re.M|re.I);

if matchObj:
    print("matchObj.group() : ", matchObj.group());
    print("matchObj.group(1) : ", matchObj.group(1));
    print("matchObj.group(2) : ", matchObj.group(2));
    print(matchObj.groups());
else:
    print("No Match!")