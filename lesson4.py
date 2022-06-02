'''
# 一、format()函数
# 1.按照顺序格式化输出
print('年龄:{}  姓名:{}'.format('张三','18岁'))

# 2、按照索引位进行格式化输出
print("{0}明天要去{1}{2}".format('小王','成都','搬砖'))

# 3. 按照参数名称进行格式化输出
print("{name}明天要去{city}{action}".format(name='小王',city='成都',action='搬砖'))

# 4.对列表进行格式化输出
print("{0[0]}明天要去{0[1]}{0[2]}".format(['小王','成都','搬砖']))

# 5.对字典进行格式化输出
dict1={'name':'小王 ','city':'成都','action':'搬砖'}
print("{name}明天要去{city}{action}".format(**dict1))  #传入的是可变字典，即可变关键词

# 二、zip()函数
list1=['name','age','class']
list2=['小王','18','1833']
a=zip(list1,list2)  #将两个列表压缩成一个zip对象，压缩以列表元素少的位标准
print(a)  #<zip object at 0x0000019456A33980>
b=dict(a)  #将zip对象转为字典格式
print(b)  #{'name': '小王', 'age': '18', 'class': '1833'}


'''


# 三、open()函数 打开txt文件。 r+path   代表这个路径不转译
o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\hello.txt','r',encoding='utf-8')
'''
Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)

'''
# encoding 代表编码格式
# 第一种模式 r 代表read 读
# 1.read()
all=o.read() #将文件中的内容读取处理，并且转成字符串
print(all)
print(type(all)) #<class 'str'>

# 2.readline()  取第一行的内容
all=o.readline()  #取出o 中的第一行
all1=o.readline()  #取出当前的第一行，因为第一行已经取走了，所以当前的第一行就是文件的第二行
print(all)  #你好
print(all1) #欢迎来到成都

# 3.readlines()  读取出所有的文件内容，并且每一行当做一个元素假如到一个列表中
all=o.readlines()
print(all)

#第二个模式 w 代表write   写入，覆盖
o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\hello.txt','w',encoding='utf-8')
# 1.write()  将内容写入到文件中，并将原文件内容进行覆盖
o.write('小王明天去搬砖\n小李明天也去搬砖')

# 第三个模式 a 代表 append  追加
o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\hello.txt','w',encoding='utf-8')
o.write('小王明天去搬砖\n小李明天也去搬砖')  #将内容追加到文件中


# 当传入的路径不存在是，那么会自己创建一个文件，并写入内容   需要使用 w 模式
o=open(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\hello1.txt','w',encoding='utf-8')
o.write('hello')

o.close()  #关闭文件  每次文件操作完成后都需要关闭对文件的操作


