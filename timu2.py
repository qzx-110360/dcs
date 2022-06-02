'''
12、分析以下数字的规律， 1 1 2 3 5 8 13 21 34用Python语言编程实现输出。  （斐波那契数列）
13、先定义一个字典来存放用户名
和密码如dic = {'admin': '123456', 'dcs46': '654321'}
要求如下：
1）、从字典中获取用户完成登入，登入时判断用户是否存在
存在直接登入
2）、如果输入的登入用户判断不存在字典，则调用注册方法，完成该用户的注册，注册成功后写入字典
定义登录函数
14、用字符串aabbcdbaaabc，用你熟悉的语言实现去除"ab"子串
15、水仙花数：一个三位数，其按位立方之和等于该数本身，该数称为水仙花数。求出100 - 1000之间的水仙花数。
其实，水仙花数是“自幂数”中的一种；自幂数：一个n位数，其按位数字的n次方之和，等于该数本身。

百位数的立方+十位数的立方+个位数的立方=这个数本身  ==》 水仙花数

16、用递归的方法求出n的阶乘？4的阶乘结果为?   （ 递归： 自己调用自己）   4 ==》 4*3*2*1
17、有如下url地址, 要求实现截取出"?"号后面的参数, 并将参数以"key value"的键值形式保存起来, 并最终通过#get(key)的方式取出对应的value值。
url地址如下：
http://ip:port/extername/get_account_trade_record.json?page_size=20&page_index=1&user_
id=203317&trade_type=0"
'''

'''
12、分析以下数字的规律， 1 1 2 3 5 8 13 21 34用Python语言编程实现输出。  （斐波那契数列）

def fid(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fid(n-2)+fid(n-1)
print(fid(10))

#第二种方式
def feb(n):
    list=[]
    for i in range(n):
        if i==0 or i==1:
            list.append(1)
        else:
            list.append(list[-1]+list[-2])
    print(list)

feb(9)    
'''

'''
13、先定义一个字典来存放用户名
和密码如dic = {'admin': '123456', 'dcs46': '654321'}
要求如下：
1）、从字典中获取用户完成登入，登入时判断用户是否存在
存在直接登入
2）、如果输入的登入用户判断不存在字典，则调用注册方法，完成该用户的注册，注册成功后写入字典
定义登录函数

dic = {'admin': '123456', 'dcs46': '654321'}

# 账号登录
def login():
    print(dic, id(dic))
    acount=input('请输入账号:')
    if acount in dic.keys():
        pwd = input("请输入密码:")
        if dic[acount] == pwd:
            print('登录成功')
        else:
            print('密码错误')
    elif acount not in dic.keys():
        print('没有此账号请注册')
        register()

# 账号注册
def register():
    acount = input('请输入账号：')
    if acount in dic.keys():  
        print('账号已经存在,请重新登录')
    else:
       pwd=input('请输入密码：')
    dic[acount] = pwd
    print('注册完成')
    login()

# 调用
login()
'''


'''
14、用字符串aabbcdbaaabc，用你熟悉的语言实现去除"ab"子串

def rm(str,str1='aabbcdbaaabc'):
    while str in str1:
        str1 = str1.replace(str, '')
    print(str1)
rm('ab')
'''




'''
15、水仙花数：一个三位数，其按位立方之和等于该数本身，该数称为水仙花数。求出100 - 1000之间的水仙花数。
其实，水仙花数是“自幂数”中的一种；自幂数：一个n位数，其按位数字的n次方之和，等于该数本身。
sum=0
for item in range(100,1000):
    ge=item%10         #个位
    shi=item//10%10    #十位
    bai=item//100      #百位
    if ge**3+shi**3+bai**3 == item:
        sum += item
print(sum)
'''

'''
16、用递归的方法求出n的阶乘？4的阶乘结果为?   （ 递归： 自己调用自己）   4 ==》 4*3*2*1
def sum(n):
    if n==1:
        return 1
    else:
        return n*sum(n-1)

s=sum(6)
print(s)
'''


'''
17、有如下url地址, 要求实现截取出"?"号后面的参数, 并将参数以"key value"的键值形式保存起来, 
并最终通过#get(key)的方式取出对应的value值。
url地址如下：
http://ip:port/extername/get_account_trade_record.json?page_size=20&page_index=1&user_id=203317&trade_type=0

url = 'http://ip:port/extername/get_account_trade_record.json?page_size=20&page_index=1&user_id=203317&trade_type=0'
url2 = url.split('?')
url3 = url2[1].split('&')
list = []
def get_key(key):
    for i in range(len(url3)):
        url4 = url3[i].split('=')
        list.append(url4)
    list1 = dict(list)
    result=list1[key]
    print(result)

get_key('page_size')
'''

# import random
# str1='1'
# num1='3456789'
# str2=random.choices(num1)[0]
# num2=random.randint(000000000,999999999)
# str3=str(num2)
# print(str1+str2+str3)

list1=[]
list=[1,1,1,2,3,4,5,5,5]
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)