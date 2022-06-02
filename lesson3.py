# 1.if判断：
# if 单分支
num=int(input("请输入一个数，"))
if num>0:
    print("您输入的大于0")
else:
    print("您输入的值不大于0")

# if多分支 输入大于0就显示大于零，输入0就等于0，输入小于0就小于0
num=int(input('请输入一个数'))
if num>0:
    print('您输入的大于0')
elif num==0:
    print('您输入的等于0')
elif num<0:
    print('您输入的值不大于0')
else:
    print('您输入的内容有误')

# 2 while循环，满足条件进入循环，不满足跳出循环
a=1
while a<100:
    print(a)
    a=a+1

'''
练习
生成100以内的整数，将他们偶数求和
'''
a=1
sum=0
while a<100:
    sum+=a
    a+=1
print(sum)

a=0
sum=0
while a<100:
    if a%2==0:
        sum+=a
    a+=1
print(sum)