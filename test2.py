'''
定义一个函数，求出6科的平均分
'''

def avge(n):
    avg=n/6
    return avg


'''
定义一个函数，将平均分进行比较得出结论
'''

def excellent():
    avg=avge(int(input("请输入总分:")))
    if avg >90:
        print("优秀学生")
    elif avg>80 and avg<90:
        print('良好学生')
    else:
        print('同志仍需努力')

# 调用，传参
excellent()