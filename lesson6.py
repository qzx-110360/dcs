
# 正则表达式
'''
预定义字符集匹配：
\d:数字0-9
\D:非数字
\s:空白字符
\n:换行符
\r:回车符
re模块数量词匹配：
符号^：表示的匹配字符以什么开头
符号$：表示的匹配字符以什么结尾
符号*：匹配*前面的字符0次或n次 eg：ab* 能匹配a 匹配ab 匹配abb
符号+：匹配+前面的字符1次或n次
符号?：匹配?前面的字符0次或1次
符号{m}：匹配前一个字符m次
符号{m,n}：匹配前一个字符m到n次(包括n次)，m或n可以省略，mn都是 正整数

'''
import  re
# re 模块相关函数
# 1.match 从第一个字符开始匹配，如果第一个字符不是要匹配的类型，则匹配失败并报错
str1=re.match('\d','1WD2WDFR2314WS') #1
str1=re.match('\d','aWD2WDFR2314WS') #报错
str1=re.match('\D','aWD2WDFR2314WS') #a
str1=re.match('\D+','aWD2WDFR2314WS') #aWD
str1=re.match('\D*','1aWD2WDFR2314WS') 空
str1=re.match('\D?','1aWD2WDFR2314WS') 空
str1=re.match('\D?','aWD2WDFR2314WS') #a
str1=re.match('\D{4}','aWD2WDFR2314WS')
str1=re.match('\D{8}','aWD2WDFR2314WS')
str1=re.match('\D{4,8}','aWD2WDFR2314WS')
str1=re.match('^1\d{4,12}','1234567aWD2WDFR2314WS')
str1=re.match('^2\d{4,12}','1234567aWD2WDFR2314WS')
str1=re.match('^1\d{4,12}\D{2}$','1234567WS')
str1=re.match('^1\d{4,12}\D{2}$','1234567WSR')

# print(str1.group())

# 2.search 从第一个字符开始查找，一找到就返回第一个字符串，找不到就不往下找，找不到后则报错
str1=re.search('\d','1WD2WFE12331WS') #1
str1=re.search('\d','WD2WFE12331WS') #2
str1=re.search('\d*','23WD2WFE12331WS') #23
str1=re.search('\d+','weigcfqevc') #报错
str1=re.search('\d?','WD2WFE12331WS') # 空
str1=re.search('\d*','WD2WFE12331WS') #空
str1=re.search('\d+','WD2WFE12331WS') #2
str1=re.search('\d{3}','WD2WFE12331WS') #123
str1=re.search('\d{5}','WD2WFE12331WS') #12331

print(str1.group())

# 3.findall 从第一个字符开始查找，找到 全部相关匹配 为止，找不到返回一个空列表[]
str1=re.findall('\d','27dsagfalda3141djsakldj421dsa') #['2', '7', '3', '1', '4', '1', '4', '2', '1']
str1=re.findall('\d{2,4}','27dsagfalda3141djsakldj421dsa') #['27', '3141', '421']
str1=re.findall('\d*','27dsagfalda3141djsakldj421dsa') #['27', '', '', '', '', ...
str1=re.findall('\d+','27dsagfalda3141djsakldj421dsa') #['27', '3141', '421']
str1=re.findall('\d?','27dsagfalda3141djsakldj421dsa')  #['2', '7', '', '', '', ''....

print(str1)

# 匹配手机号 [3~9] 3和9  [3-9]3到9
str1=re.findall('^1[3-9]\d{9}','18142503296WEASDASWAFSF78#@WFAS')

# 匹配指定内容
str1=re.findall('error','uwaeaerrorwadsaderrorsdjalkferrorsda')

# 贪婪匹配  匹配尽可能多的符合条件的内容  "." 代表任意字符
# 非贪婪匹配  一旦遇到符合条件就返回
str1='<strint>北京</strint><strint>天津</strint><strint上海</strint><strint>重庆</strint>'
# str2=re.findall('<strint>(.+)</strint>',str1) #['北京</strint><strint>天津</strint><strint上海</strint><strint>重庆']
str2=re.findall('<strint>(.+?)</strint>',str1) #['北京', '天津', '重庆']
print(str2)

# 4.compile  编译模式生成对象，找到全部相关匹配为止，找不到返回一个列表
str1=re.compile('error')
str2=str1.findall('uwaeaerrorwadsaderrorsdjalkferrorsda')
print(str2) #['error', 'error', 'error']