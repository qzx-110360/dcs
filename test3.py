'''
18、存在一个文件, 文件名test.txt
内容如下：
01 success
02 fail
03 fail
04 success
....请使用Python语言编写程序实现统计该文件中
有多少个success
多少个fail的功能？
19、一个txt文件中已知数据为：
C4D
C4D/maya
C4D
C4D/su
C4D/max/AE
统计每个字段出现的次数，比如C4D,maya,su,max,AE 请用最熟悉的语言或者伪代码实现该需求
20、统计一个文件的行数，以e:\\write.txt文件为例(内容自己建)
'''

'''
18、存在一个文件, 文件名test.txt
内容如下：
01 success
02 fail
03 fail
04 success
....请使用Python语言编写程序实现统计该文件中
有多少个success
多少个fail的功能？


'''
# o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\test.txt','w',encoding='utf-8')
# o.write('01 success\n02 fail\n03 fail\n04 success')
# o.close()
#
# o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\test.txt','r',encoding='utf-8')
# str1=o.read()
# print(str1.count('fail'))
# print(str1.count('success'))


'''
19、一个txt文件中已知数据为：
C4D
C4D/maya
C4D
C4D/su
C4D/max/AE
统计每个字段出现的次数，比如C4D,maya,su,max,AE 请用最熟悉的语言或者伪代码实现该需求


'''

#o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\test1.txt','w',encoding='utf-8')
# o.write('C4D\nC4D/mayal\nC4D\nC4D/su\nC4D/max/AE')
# o.close()

# o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\test1.txt','r',encoding='utf-8')

# ['C4D\n', 'C4D/mayal\n', 'C4D\n', 'C4D/su\n', 'C4D/max/AE']

#取出字符串
# def get_value():
#     str2 = o.read()
#     str3 = str2.split('\n')  #按照"\n"分隔为列表
#     for i in range(len(str3)):
#         if '/' in str3[i]:  #"将列表中含有'/'的字符串进行分隔
#             str4=str3[i].split('/')
#             for j in range(len(str4)):
#                 list1.append(str4[j]) #将分割后的字符串添加进列表
#     set1=set(list1)  #去重
#     for h in set1: #遍历集合的内容，将内容的个数输出
#         print(h,str2.count(h))
#
# list1=[]
# get_value()

# dict1={}
# o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\test1.txt','r',encoding='utf-8')
# str1=o.readlines()
# for i in str1:
#     str1=i.replace('\n','')
#     str1=str1.split('/')
#     for j in str1:
#         if j not in dict1.keys():
#             dict1[j]=1
#         else:
#             dict1[j]=dict1[j]+1
# print(dict1)

'''
# 20、统计一个文件的行数，以e:\\write.txt文件为例(内容自己建)
'''
s=0
o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\test1.txt','r',encoding='utf-8')
str2=o.readlines()
# print(str2)
for i in str2:
    if '\n' in i:
       s=s+1
print(s+1)

# 第二种
o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\test1.txt','r',encoding='utf-8')
str2=o.readlines()
if '\n' in str2[-1]:
    print(len(str2)+1)
else:
    print(len(str2))