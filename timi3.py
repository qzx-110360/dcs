'''
21、使用os模块写一个递归调用打印出e:\\home下的所有文件名的绝对路径？
22、用正则方法实现统计e:\\python文件中指定字符如"python"的行数?（文件中的python字符）
假设里面的数据为：
pythonelloerrorpythonpythonpython
warnipythonngerror
warning
errorwapythonrning
23、使用正则完成市面上手机规则的编写、随机生成11位数然后通过正则匹配出
符合规则的11位数手机号码？（手机号：11位）
24、用正则实现写一段代码统计e:\\log文件中error和warning单词出现的次数分别为几次?
文件内容如下：
warningabchelloerrorwarningwarning
warningerror
warning
errorwarningwarning

25、
str1='{"name":"xiaowang","age":"18岁"}'
# 要求从从str1中，匹配出每一个值： "xiaowang" 和"18岁"

'''
# 21、使用os模块写一个递归调用打印出e:\\home下的所有文件名的绝对路径？
# C:\Users\admin\PycharmProjects\duoceshi

import os
def get_path(path):
    all=os.listdir(path)
    for i in all:
        new_path=os.path.join(path,i)
        if os.path.isfile(new_path):
            print(new_path)
        else:
            print(new_path)
            get_path(new_path)

get_path('d:\Python')

'''
22、用正则方法实现统计e:\\python文件中指定字符如"python"的行数?（文件中的python字符）
假设里面的数据为：
pythonelloerrorpythonpythonpython
warnipythonngerror
warning
errorwapythonrning
'''
import re
def get_rows(file,word):
    o=open(file,'r')
    all=o.readlines()
    count=0
    for i in all:
        a=re.findall(word,i)
        if len(a) !=0:
            count+=1
    print('{0}在文件中出现的行数为{1}行'.format(word,count))

get_rows(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\bb.txt','python')
'''
23、使用正则完成市面上手机规则的编写、随机生成11位数然后通过正则匹配出
符合规则的11位数手机号码？（手机号：11位）
'''
import random
import re

while True:
    result = random.randint(00000000000, 99999999999)
    str2 = str(result)
    if len(re.findall('^1[3-9]\d{9}?',str2)) !=0:
        print(re.findall('^1[3-9]\d{9}?',str2)[0])
        break


'''
24、用正则实现写一段代码统计e:\\log文件中error和warning单词出现的次数分别为几次?
文件内容如下：
warningabchelloerrorwarningwarning
warningerror
warning
errorwarningwarning
'''


o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\aa.txt','r',encoding='utf-8')
result=o.read()
import re

def get_num(str):
    if re.findall(str+'*',result) is not None:
        es = re.findall(str+'*', result)
        print(str+'出现的次数为:{0}次'.format(len(es)))
    else:
        print('0')

get_num('warning')

'''
25、
str1='{"name":"xiaowang","age":"18岁"}'
# 要求从从str1中，匹配出每一个值： "xiaowang" 和"18岁"
'''
import re
str1='{"name":"xiaowang","age":"18岁"}'

str2=re.findall(':"(.+?)"',str1)
print(str2)

import json
a=json.loads(str1)   #将字符串中长得像字典的转换为字典
print(a)