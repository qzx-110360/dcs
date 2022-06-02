'''
# 函数的参数传递

def fun(arg1,arg2):
     print('agr1',arg1)
     print('arg2',arg2)
     print(id(arg1))
     arg1=100
     print(id(arg1))
     arg2.append(10)
     print('agr1',arg1)
     print('arg2',arg2)


# 函数的调用，传入实参
n1=11
n2=[22,33,44]
fun(n1,n2)
print('n1',n1)
print('n2',n2)

'''



'''
在函数调用过程中，进行参数的传递

如果是不可变对象，在函数体的修改不会影响实参的值
如果是可变对象，在函数体的修改会影响实参的值


判断可变还是不可变的依据是，在内存空间中，如果参数改变后，是否会在内存中开辟一块新的空间来存储这个数据（通过id来判断）如果id值改变，说明开辟了新的空间
那么这个数据类型是不可变对象，如果id值没有改变，说明是在原来的内存中进行了增加，说明是可变对象
'''


'''

# 函数的多个返回值
# 返回的值是元组
def fun(num):
    odd=[]  #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

#函数的调用
lst=[10,29,34,23,44,53,55]
print(fun(lst))

'''


'''
函数的返回值
（1）如果函数没有返回值（函数执行完毕后，不需要给调用处提供数据）return 可以省略不写
（2）函数的返回值，如果是1个，直接返回类型
（3）函数的返回值，如果是多个返回的结果为元组
1.
def fun1():
    print('hello') 

fun1()  #hello

2.
def fun2():
    return 'hello'

res = fun2()
print(res)   #hello


3.
def fun3():
    return 'hello', 'world'

print(fun3())  #('hello', 'world')
'''


'''
def fun(*args):  # 函数定义时的，可变的位置参数，只能有一个
    print(args)

fun(10)
fun(20, 30)
fun(30, 40, 50)


def fun1(**args):  #定义个数可变的关键字参数，只能有一个
    print(args)

fun1(a=10)
fun1(a=20,b=30,c=40)


既有个数可变的位置形参，和个数可变的关键字形参时，需要将位置形参放在关键字形参之前
def fun2(*args1,**args2):
    pass

'''

'''

def fun(a,b):
    c=a+b     #c就是局部变量，因为c是在函数体内定义的变量，a,b为函数的形参，作用范围也是函数体的内部
    print(c)


# print(a)  NameError: name 'a' is not defined
# 报错原因，a的作用范围是函数体内部（超出了作用域）

'''
'''
递归调用
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))
'''

# try:
#     n1=int(input('请输入'))
#     n2=int(input('请输入'))
#     result=n1/n2
#     print('结果为',result)
#
# except ZeroDivisionError:
#     print('除数不能为0')


#traceback  模块
# import traceback
# try:
#    print('----------')
#    num=10/0
# except:
#     traceback.print_exc()




