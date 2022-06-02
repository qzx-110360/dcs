ACOUNT = "admin"
PASSWORLD = 123456


account = input("请输入账号：")
if account == ACOUNT:
    passworld=int(input("请输入密码："))
    if passworld == PASSWORLD:
        print("登录成功")
    else:
        print("密码错误")
elif account != ACOUNT:
    print("账号不存在")




dict1={"admin":123456,"user1":654321,"user2":67890}

accout=input("请输入账号：")
if accout in dict1.keys():
    pwd = int(input("请输入密码："))
    if pwd==dict1[accout]:
        print("密码正确")
    else:
        print('密码错误')
else:
    print("账号错误")
