'''
python自带的函数
字符串函数
列表的函数
元组的函数
字典的函数
集合的函数
'''
# 一、python中操作字符串的函数
str1='asdfghjkala'
# 1.capitalize()函数，首字母大写
print(str1.capitalize())  #Asdfghjkala

# 2. title()函数
print(str1.title()) #Asdfghjkala  会将每一个单词的首字母大写

# 3.replace()函数，第一个参数代表被替换的内容，第二个参数代表要替换成的内容
# 第三个代表从左到右替换的次数，替换次数不写，那么将全部替换
print(str1.replace('a','*',2)) #*sdfghjk*la6

# 4.split()函数，通过指定内容进行分割。并且加入到一个列表当中
print(str1.split('h')) #['asdfg', 'jkala']

# 5.count()函数 。统计字符串中指定内容出现的次数
print(str1.count("a")) #3

# 6.join()函数，指定内容，用于将str1进行拼接
print("*".join(str1)) #a*s*d*f*g*h*j*k*a*l*a

# 7.strip（）函数，删除收尾的指定内容
print(str1.strip('al')) #sdfghjk

# 8.lstrip() 删除开头
print(str1.lstrip("a"))  #sdfghjkala

# 9.rstrip() 删除结尾
print(str1.rstrip("a")) #asdfghjkal

'''
练习
有一个字符串：user_name，需要将字符串转为UserName
'''
str2="user_name"
print(str2.title().replace("_",""))

# 10.find() 函数
str1='asdfghjkal'
print(str1.find("a"))  #返回指定内容的索引下标，从左往右查找
print(str1.rfind("a")) #返回指定内容的索引下标，从右往左查找
print(str1.find("a",4,9)) #指定区间，查看指定内容的索引

# 11.starswith() 函数：判断以什么开头
print(str1.startswith("a"))  #True

# 12.endswith() 函数：判断以什么结尾
print(str1.endswith("a")) #False

# 13.istitle()判断字符串是否是首字母大写
print(str1.istitle()) #True

# 14.isupper()判断字符串是否全部为大写
print(str1.isupper())

# 15. islower()判断字符串是否全部为小写
print(str1.islower())

# 16.isdigit()判断是否全部为数字
print(str1.isdigit())

# 17.isalnum() 判断是否全部为字母和数字
print(str1.isalnum())

# 18.isalpha() 判断是否全部为字母
print(str1.isalpha())

# 19.upper() 函数 将字符串的内容 全部为大写
print(str1.upper())

# 20.lower() 函数，将字符串的内容 全部为小写
print(str1.lower())


# 二、python中操作列表的函数：
# 第一种定义列表的方式
list1=[1,2,3,"4","5",['四川','成都']]

# 第二种定义方式
str1='asdfgh'
a=list(str1)
print(a)

# 1.给列表赋值
list1=[1,2,3,"4","5",['四川','成都']]
print(list1[5]) #['四川', '成都']

# 通过索引位赋值
list1[0]='china'
print(list1) #['china', 2, 3, '4', '5', ['四川', '成都']]

# 2.通过切片赋值
list1[2:4]='abc'
print(list1) #['1', 2, 'a', 'b', 'c', '5', ['四川', '成都']]

# 3.对列表的子对象进行赋值
list1[5][1]='chengdu'
print(list1)

# 2.append()函数 在列表的最后添加元素
list1=[1,2,3,"4","5",['四川','成都']]
list1.append("china")

# 3 insert() 函数，往指定索引位地方插入值
list1.insert(0,"小王")

# 4. remove() 函数，移除从左往右第一个指定的元素
list1=[1,2,3,"4","5",['四川','成都']]
list1.remove(1)

# 5.sort() 函数，列表的排序，升序
list1 =[1,34,15,21,7,16]
list1.sort()
list1.sort(reverse=True)

# 6.sorted()函数，reverse反转，true就是反转，FALSE就是不反转
list1 =[1,34,15,21,7,16]
print(sorted(list1,reverse=True))

# 字符串之间比较用 Ascll 码比较  0~9  A~Z a~z
list1=['1','34','15','021','7','BU','bi','ac']
list1.sort()
print(list1)

# 列表反转
list1=[1,2,3,"4","5",['四川','成都']]
print(list1[::-1]) #切片反转输出
list1.reverse()  #用函数反转列表
print(list1)

# del 关键字  通过索引下标，删除指定内容
list1=[1,2,3,4]
del list1[1]
print(list1)


# inde（）函数
# list1=[“1”,2,3,“1”，"4","5",['四川','成都']]
# print（list.index("1")） 查找元素 “1”的索引位
# print（list.index("1",2,4) 在范围2~4之间查找元素 “1” 的索引位

# pop函数：
# list1=[“1”,2,3,“1”，"4","5",['四川','成都']]
list1.pop()  #随机删除列表中的元素，但是一般是删除最后一个
list1.pop(1)  #删除类别中索引位为1 的值，并且将删除的值返回

#三、python中的元组： 用（）当元组的内容只有一个时，必须要加 , 号说明，表明是元组，元组的内容不能修改
#定义元组方式一
tuplel=(1, 2, 3, 4)
print(type(tuplel))  #<class,tuple>

#定义元组方式二：
# str1=“hello”
a=tuple(str1)

#1.列表转元组
list1=['h','e','l','l','o']
tuple(list1)

#2.元组转列表
#tuplel=(['h','e','l','l','o')
list1 = list(tuplel)
print(list1)

# 3.修改元组，将“天府新区”改为“tianfu”
tuplel=('china','sichuan','chengdu','shuangliu','天府新区')
list1=list(tuplel)
list1[4]='tianfu'
print(list1)
print(tuple(list1))

# 4.修改元组中子对象的值
# 将"武侯" 添加到tuple1中的列表中去
tuple1=('china','sichuan','chengdu'['金牛','锦江','成华','青羊'])
tuple1[3].append('武侯')
print(tuple1)
'''
# 三.python中的字典：
1. 用{ }表示，字典的内容是以键值对的形式存在的 key：value
2. 字典中的键名都必须是字符串格式，值了仪式任意的数据类型
3.字典键健名不能重复
4. 字典不能支持索引取值，字典是无序的
'''
#1.定义字典的第一种方式
dict1={"name":"小王","age":"18岁","class":1833}
print(dict1)

# 2.定义字典的第二种方式 dict()  必须要使用特定格式的列表或元组
list=(["name","xiaowang"],["age","18岁"],["class",1833])
dict1= dict(list)
print(dict1)

#3.根据键名取值
dict1={"name":"小王","age":"18岁","class":1833}
print(dict1["name"])   #小王
print(dict1["age"])   #18岁
print(dict1["class"])   #1833

# 4.修改字典中键对应的值
dict1={"name":"小王","age":"18岁","class":1833}
dict1['name']='小李' #如果字典存在name这个键名，那么值就会被覆盖

dict1['sex']='男' #如果键名不存在，会添加一个键值对

# 5. setdefault 给字典添加键值对，如果键名存在，会设置无效
dict1={"name":"小王","age":"18岁","class":1833}
dict1.setdefault('name','男')

# 6. 删除字典中的键值对
dict1={"name":"小王","age":"18岁","class":1833}
del dict1['name'] #删除字典中指定的键值对

del dict1  #删除整个字典

# 7. 取出字典中所有的键名
dict1={"name":"小王","age":"18岁","class":1833}
dict1.keys()
print(type(dict1.keys()))
for i in dict1.keys():  #取出所有的键名
    print(i)

# 取出字典中所有的值
dict1={"name":"小王","age":"18岁","class":1833}
# 第一种：
print(dict1.values())
for j in dict1.values():
    print(j)

# 第二种：
for i in dict1.keys():
    print(dict1[i])  #dict1[i] 根据键名取值 == print(dict1["name"])

#9.清空字典 clear()
dict1={"name":"小王","age":"18岁","class":1833}
dict1.clear() #将字典中所有的内容清空，但是会保留字典的定义

# 10.更新字典
dict1={"name":"小王","age":"18岁"}
dict2={"class":1833}
dict1.update(dict2)

#11.fromkeys()  用来初始化字典
a={}.fromkeys(['name','class'],'hello') #第一个是键，第二个是值

#12 __contains（） 判断字典中是否有这个键名
dict1={"name":"小王","age":"18岁","class":1833}
print(dict1.__contains__('name')) #True

# 13 pop（）函数，删除指定的键值对 ，返回键对应的值
dict1={"name":"小王","age":"18岁","class":1833}
dict1.pop('name')

# 14.popitem() 函数 删除时返回被删除的键值对
dict1.popitem()

for i in dict1.items():
    print(i)   #返回字典的键值对，返回类型为元组
    print(i,type(i)) #class，tuple

# 15 get() 函数
dict1={"name":"小王","age":"18岁","class":1833}
dict1.get('name')  #通过存在的键名取值，不存在的键名，返回none
dict1['name']  #通过键名取值，不存在的报错

#四。python中的集合 set 表示 符号{}  集合最大的作用就是去重，并且集合是无序的
# 1。定义集合的第一种方式
set1={1,23,3,4,5,6,7,6,6,6,6,'hello','hello'}

# 2. 定义集合的第二种方式
str1='lehekkkhefoo'
set1=set(str1)  #通过set 将字符串转为集合

# 3、add() 函数，给集合添加内容
set1={1,23,3,4,5,6,7,6,6,6,6,'hello','hello'}
set1.add(888)

# 4.clear()函数，清除集合的内容
set1={1,23,3,4,5,6,7,6,6,6,6,'hello','hello'}
set1.clear()

# 5.remove() 移除元素
set1={1,23,3,4,5,6,7,6,6,6,6,'hello','hello'}
set1.remove('hello')

# 6.pop函数
set1={1,23,3,4,5,6,7,6,6,6,6,'hello','hello'}
print(set1.pop()) #删除集合中的第一个元素，并返回值

# 不可变集合， 集合的内容不可变
str1='lehekkkhefoo'
set1=frozenset(str1)
set1.add(1)  #报错，不能添加
a=set1.copy()  #不可变集合可以copy（）
