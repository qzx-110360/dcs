# 1.python中的格式化输出
# python中的数据类型
#     内置数据类型
#     在编程中，数据类型是一个重要的概念。
#
#     变量可以存储不同类型的数据，并且不同类型可以执行不同的操作。
#
#     在这些类别中，Python 默认拥有以下内置数据类型：
#
#     文本类型：	str
#     数值类型：	int, float, complex
#     序列类型：	list, tuple, range
#     映射类型：	dict
#     集合类型：	set, frozenset
#     布尔类型：	bool
#     二进制类型：	bytes, bytearray, memoryview
# int： 123 整数型
# str： 'a '符型  'ab'字符串型
# %s 字符串（采用str（）的显示）
city="成都"
print("欢迎来到%s"%city)

# %c 单个字符
num="1"
print("china is number %c"%num)

# %d 十进制整数
num=1
print("china is number %d"%num)

# %i 十进制整数
num=1
print("china is number %i"%num)

# %o 八进制整数
num=20
print("num的八进制对应的值是：%o"%num)

# %x 十六进制整数
num=20
print("num的十六进制对应的值是：%x" %num)

# %% 字符%
num=60
print("本次考试的及格率为%d%%"%num)


# 同时引用多个变量
num=1
country = "china"
print("%s is number %d"%(country,num))

# 2.python中的注释
# 1.单行注释  # 快捷键 ctrl+/
# 2.用引号注释：单引号，双引号，三引号

# 单引号，和双引号，一般用于定义字符串
# 三引号一般用于注释

# 三引号
print('''china is number '''1''' ''') #三引号不能注释三引号
print('''china is number "1" ''') #三引号可以包含双引号
print('''china is number '1' ''') # #三引号可包含单引号

#双引号
print("china is number '''1''' ") #双引号可以包含三引号
print("china is number "1" ") #双引号不可以包含双引号
print("china is number '''1''' ") #双引号可以包含单引号

#单引号
# print('china is number '''1''' ') #单引号不可以包含三引号
print('china is number "1" ') #单引号可以包含双引号
print('china is number '1' ') #单引号不可以包含单引号


# 3.python中变量命名的规则

'''
1、变量由字母，数字，下划线组成，但必须是字母或下划线开头，区分大小 写，
不能由数字开头

2、下划线和大写字母开头的标识符有特殊意义： 
a.单下划线开头标识符_xxx 不能用于from xxx import *，即保护类型只能允 
许其本身与子类进行访问 
b.__xxx 双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访 问了，
连子类也不可以 
c.大写字母开头的在Python中一般表示类比如：People
'''

#4. python中的输入函数：input函数，  会将输入的内容分偶的转为字符串格式
username = input("请输入您的名字：")
if username == "小刘":
    print("hello")
else:
    print("欢迎")

num= int(input("请输入您的分数："))  #用int将如输入的数字转为整数型
if num >= 90:
    print("优秀学生")
elif num >= 80 :
    print("良好学生")
else:
    print("仍需努力")

# python中的运算符
a=5
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  #地板除，只取整数部分
print(a%b)  #取模，也叫取余
print(a**b)  #取幂

# python中的比较运算符
print(a>b)
print(a<b)
print(a>b or a<b)  #或者，满足其中一个，就为真
print(a>b and a<b) # 和，需要同时满足多个条件就为真
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# python中的赋值运算
# a+=1  ==> a=a+1
a+=b
a-=b
a*=b
a/=b
a%=b
a//=b
print(a)

python中的成员运算符，判断XXX是否在XXX之中
list1 = [1,2,3,4,5,6,"7","8"]
print(1 in list1)  #True
print(1 not in list1) #False
print(7 not in list1) #True


# python中的位运算符
'''
1TB = 1024GB
1GB = 1024MB
1MB = 1024KB
1KB = 1024byte
1byte = 8bit 位
二进制
0     0   0   0   0   0  0  0 
128  64   32  16  8   4  2  1
 
'''

a=11  #00001011
b=5   #00000101
# 1.按位与  将两个十进制的数转为二进制，比较两个的位，如果都是1，则取1，否则取0
print(a&b)  #00000001   1
# 2.按位或  将两个十进制的数转为二进制，比较两个的位，有一个为1，则取1，否则取0
print(a|b)  #00001111   15
# 3.按位异或，将两个十进制的数转为二进制，比较两个的位，当两个为不相同时取1，否则取0
print(a^b)  #00001110  14
# 4.按位取反 -（x+1）
print(~a)  # -12
# 5.移位
print(a>>2)  # 00000010 2  向右移两位
print(a<<2)  # 00101100 44 向左移两位


# python中的索引：索引下标，来标明现在所处的位置
# 索引有正负之分，正向索引从左往右，从0开始，负向索引从右往左，从-1开始
'''
str1="asdfghjkl"
print(str[1])  # s
print(str[-4]) # h
print(str[10])  #string index out of range ,索引越界
'''

'''
# 2.索引切片
a.切片建立在索引之上
b.切片的公式[start_index:end_index:setp]
start_index 代表从该位置开始取
end_index   代表取到这个地方，但是本身取不到
setp        代表步长，默认值1，当为n的时候，就是隔n个取一个
步长有正负之分，正向代表从左往右取，负向代表从右往左取
'''

str1="asdfghjkl"
print(str1[1:6]) #sdfgh
print(str1[-6:-2]) #fghj
print(str1[1:6:3]) #sg
print(str1[1:6:-1]) #空值
print(str1[-1:-6:1]) #空值
print(str1[:-2:-1]) # l
print(str1[:-2])  #asdfghj
print(str1[1::-1]) #sa
print(str1[-1::-1]) #lkjhgfdsa
print(str1[2:-3:-1]) #空值
print(str1[::-1]) # 反转输出 lkjhgfdsa



