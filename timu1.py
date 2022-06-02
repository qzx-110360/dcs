'''
1、求出1 / 1 + 1 / 3 + 1 / 5......+1 / 99的和
2、用循环语句，计算2 - 10之间整数的循环相乘的值。
3、用for循环打印九九乘法表
4、求每个字符串中字符出现的个数如：helloworld
5、实现把字符串str = "duoceshi"中任意字母变为大写、在输入函数中输入DCE输出结果为：DuoCEshi
6、求出1900 - 2017年的闰年？
普通闰年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1999年不是闰年）
世纪闰年:能被400整除的为世纪闰年。（如2000年是世纪闰年，1900年不是世纪闰年）
7、分别打印100以内的所有偶数和奇数并存入不同的列表当中
8、请写一段Python代码用for循环实现对list = [1, 3, 6, 9, 1, 8]里面的元素进行去重 (不能用集合)
9、利用for循环把字符串user_controller转换为驼峰命名UserController
10、选择排序
给一组无规律的数据从大到小或从小到大进行排序如：list = [2, 6, 9, 10, 18, 15, 1]
'''

'''
1、求出1 / 1 + 1 / 3 + 1 / 5......+1 / 99的和

a=1
b=0
sum=0
while a<100:
    if  a%2!=0:
        b=1/a
        sum=sum+b
    a=a+1
print(sum)
'''


'''
2、用循环语句，计算2 - 10之间整数的循环相乘的值。
b=2
sum=1
while b<10:
    sum = sum * b
    b = b + 1
print(sum)
'''



'''
3、用for循环打印九九乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={i*j}\t',end=' ')
#     print()
'''


'''
4、求每个字符串中字符出现的个数如：helloworld
str1='helloworld'
formatlist=[]
for i in str1:
    count=str1.count(i)
    list1=list[i,count]
    if list1 not in formatlist:
        formatlist.append(list1)
print(formatlist)
'''

'''
5、实现把字符串str = "duoceshi"中任意字母变为大写、在输入函数中输入DCE输出结果为：DuoCEshi
str = "duoceshi"
list1=list(str)
print(list1)
inp=input('请输入需要大写的字母:')
for i in inp:
   c=i.lower()
   a=list1.index(c)
   str2=list1[a].upper()
   list1[a]=str2

print(" ".join(list1))


'''



'''
6、求出1900 - 2017年的闰年？
for year in range(1990,2018):
    if year%4==0 and year%100!=0:
        print("普通闰年是：",year)
    elif year%400==0:
        print("世纪闰年是：",year)
'''

'''
7、分别打印100以内的所有偶数和奇数并存入不同的列表当中

a=0
list1=[]
list2=[]
while a<100:
    if a%2==0:
       list1.append(a)
       a = a + 1
    else:
        list2.append(a)
        a = a + 1
print(list1)
print(list2)
'''

'''
8、请写一段Python代码用for循环实现对list = [1, 3, 6, 9, 1, 8]里面的元素进行去重 (不能用集合)

formatlist=[]
list = [1, 3, 6, 9, 1, 8]
for id in list:
    if id not in formatlist:
        formatlist.append(id)
print(formatlist)
'''


'''
9、利用for循环把字符串user_controller转换为驼峰命名UserController
str1='user_controller'
s2=''
list1=str1.split('_')
for i in range(0,len(list1)-1):
    s1=list1[i].capitalize()
    s2=s1+list1[i+1].capitalize()
    print(s2)

'''

'''
10、选择排序
给一组无规律的数据从大到小或从小到大进行排序如：list = [2, 6, 9, 10, 18, 15, 1]

list = [2, 6, 9, 10, 18, 15, 1]
# 设置一个变量，假如此变量为最小值，进行比较，如果min> a 则说明a是最小值，然后将两个值进行交换
for i in  range(len(list)):
    min=i
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            min=j

    list[min],list[i]=list[i],list[min]

print(list)
'''




