
#类的创建
# class Student: #Student为类的名称，其余小写，由一个或多个单词组成，每个单词的首字母大写
#     pass


# 注意：静态方法只能调用类的静态属性，类方法只能调用类的静态方法和静态属性
# 实例方法的self指的是实例对象，类方法的self指的是类的元数据（类的自身）
# self的英文含义就是“自己”的意思

#类的组成：
# 类属性
class Student:
    native_pace='吉林'#直接写在类里的变量，称为类属性
    def __init__(self,name,age):  # 初始化
        self.name=name  #self.name 称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age=age
#实例方法, 在类之外定义的称为函数，在类之内定义的称为方法
    def eat(self):
        print('学生在吃饭..')
#静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
#类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

#创建Student类的对象
'''
stu1=Student('张三',20)
print(id(stu1))    #2079727377184  开辟了内存空间
print(type(stu1))  #<class '__main__.Student'> 类的类型class
print(stu1)        #<__main__.Student object at 0x000001E439695B20>  对象的值，指向了类的地址
print('-----------------')
print(id(Student))  #2079720864000
print(type(Student)) #<class 'type'>
print(Student)      #<class '__main__.Student'>
'''

#方法的调用
stu1=Student('张三',20)
stu1.eat()      #对象名.方法名
print(stu1.name)  #打印实例属性
print(stu1.age)

Student.eat(stu1)  #与eat(self)代码功能相同，都是调用Student的eat方法
                   #类名.方法名(类的对象)--->实际就是方法定义处的self

#类属性的调用方式
stu1=Student('张三',20)
stu2=Student('李四',21)
print(stu1.native_pace)  #吉林
print(stu2.native_pace)  #吉林

Student.native_pace='天津'
print(stu1.native_pace)  #天津
print(stu2.native_pace)  #天津

#类方法的调用方式
Student.cm()

#静态方法的调用方式
Student.method()

