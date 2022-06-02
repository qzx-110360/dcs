# # socre=int(input("请输入你的成绩:"))
# # if socre >= 90 and socre <= 100:
# #     print("A")
# # elif socre >= 80 and socre < 90:
# #     print("B")
# # elif socre >= 60 and socre <80:
# #     print("C")
# # elif socre >= 0 and socre < 60 :
# #     print("D")
# # else:
# #     print("不满足要求")
# #
# #
# # range()的三种创建方式
#
#
# '''
#     第一种，只有一个参数（小括号只给了一个数）
# '''
# r=range(10)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(r) #rang(0,10)
# print(list(r))
#
# '''
# 第二种创建方式，给了两个参数（小括号中给了两个数）
# '''
# r=range(1,10) #指定了起始值，从1开始，到10结束（不包含10），默认步长为1
# print(r)
#
#
# '''
# 第三种创建方式，给了三个参数（小括号三个数）
# '''
# r=range(1,10,2)
# print(r) #[1,3,5,7,9]
#
# # while 循环
# a=1
# while a<10:
#     print(a)
#     a+=1
#
# # 累加 1到4的累加
# sum=0
# a=0
# while a<5:
#     sum=sum+a
#     a=a+1
# print(sum)
#
#
#
# '''
# 练习：
# 计算1-100之间偶数相加的和
# '''
# sum=0
# a=0
# while a<101:
#     if a%2==0:
#         sum += a
#     else:
#        pass
#     a += 1
# print(sum)
#
#
#
# '''
# # for -in循环
# for-in 的语法结构
#   for自定义变量 in 可迭代对象
#     循环体
# '''
# # for循环计算1-100的偶数和
# sum=0
# for item in range(1,101):
#     if item%2==0:
#         sum+=item
#
# print(sum)
#
#
#
# '''
# 练习题：
# 输出100-999之间的水仙花数
# 例;
# 153=1*1*1+5*5*5+3*3*3
# '''
# sum=0
# for item in range(100,1000):
#     ge=item%10         #个位
#     shi=item//10%10    #十位
#     bai=item//100      #百位
#     if ge**3+shi**3+bai**3 == item:
#         sum += item
# print(sum)
#
# # break 结束语句
# # while循环
# a=0
# while a<3:
#     pwd=input("请输入密码")
#     if pwd=="888888":
#         print("密码正确")
#         break
#     else:
#         print("密码错误")
#
#     a+=1
# # for 循环
# for item in  range(3):
#     pwd=input("请输入密码：")
#     if pwd=="888888":
#         print("密码正确")
#         break
#     else:
#         print("密码错误")


# 字典
'''
key的判断  in  not in
socres.get('张2')  获取不存在的键不会报错会返回none
socres['张2']    获取不存在的键会报错 keyerror


字典的删除  del删除指定键值对  clear()清空
字典的添加  socres['陈六']=98
获取字典所有的键   key()
获取字典所有的值   value()
获取字典所有的键值  items()
'''
socres={'张三':98,'李四':95,'王五':91}

# print('张三' in socres)
# print('张三' not in socres)

#
# del socres['张三']  #删除指定的key-value 对
# print(socres)
#
# socres.clear()  #清空字典
# print(socres)
#
# socres['陈六']=98   #增加字典
# print(socres)
#
# socres['陈六']=100  #修改字典
# print(socres)

keys=socres.keys()  #获取字典所有键
print(keys)
ls=list(keys)
print(ls)

values=socres.values() #获取字典所有的值
print(values)

items=socres.items() #获取字典键值对 #[('张三', 98), ('李四', 95), ('王五', 91)]
# 得出的答案是列表中的三对元组
print(items)
ls=list(items)
print(ls)
print(ls[1])

'''
字典元素的遍历
'''
