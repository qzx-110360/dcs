'''

#动态绑定属性和方法

class Student:
    def __init__(self,name,age):  #初始化类属性
        self.name=name
        self.age=age

    def eat(self):
        print(self.name+'吃饭')


# 实例化类对象
stu1=Student('张三',20)
stu2=Student('李四',21)

# 调用对象的方法
stu1.eat()
stu2.eat()

# 为stu2对象动态绑定性别属性，只能有stu2对象才有此属性，stu1对象没有此属性
stu2.gender='女'
print(stu2.name,stu2.age,stu2.gender)


def show():
    print('定义在类之外的叫函数')

# 单独为stu1动态绑定方法,当函数被类绑定后，会将此函数变成类中的实例方法，这时候类对象可以调用此方法
stu1.show=show
stu1.show()
'''


'''
# 封装
class Student():
    def __init__(self,name,age):
        self.name=name
        self.__age=age   #将age私有化（private）这样就不允许类以外的方法来调用age属性 用__

    def show(self):  #定义一个方法，可以查看类中的age属性
        print(self.name,self.__age)




# 实例化对象
stu1=Student('张三',20)
stu2=Student('李四',21)

# 调用show方法
stu1.show()
Student.show(stu2)


# print(dir(stu1))  查看stu1这个实例对象有哪些可以使用的属性，一般不建议使用
print(stu1._Student__age)  在类的外部可以通过 _Student__age 进行访问
'''

'''
# 继承
class Person(object):  #定义一个父类 Person
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(self.name,self.age)


class Student(Person):  #定义一个子类Student,继承Person类
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):  #定义一个子类Student,继承Person类
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear


stu=Student('张三',20,1001)
teacher=Teacher('李四',34,10)

stu.info()
teacher.info()


# 多继承
class A(object):
    pass

class B(object):
    pass

class C(A,B):   #C类同时继承了A类和B类
    pass
'''

'''
 
#方法的重写
# 如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重写编写
# 子类重写后的方法中，可以通过supper().XXX()调用父类中被重写的方法
class Person(object):  #定义一个父类 Person
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(self.name,self.age)


class Student(Person):  #定义一个子类Student,继承Person类
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super().info()  #调用父类的方法
        print(self.stu_no,end=' \t') #重写父类的方法

class Teacher(Person):  #定义一个子类Student,继承Person类
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print(self.teachofyear,end=' \t')




stu=Student('张三',20,1001)
teacher=Teacher('李四',34,10)

stu.info()
teacher.info()
 '''


'''
#Object对象
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return ('我的名字叫{name},我今年{age}岁了'.format(name=self.name,age=self.age))

stu=Student("张三",20)
print(dir(stu))
print(stu)  #默认会调用__str__()这样的方法
print(stu)
'''

'''
# 多态
# 多态就是“具有多种形态”它指的是：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法
# 在运行过程中，根据变量所引用对象的类型，动态决定调用哪个对象中的方法

class Animal():
    def eat(self):
        print('动物吃....')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头....')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼....')

class Person():
    def eat(self):
        print('人吃五谷杂粮')

# Dog 和 Cat类都是继承的Animal类，但是创建的函数可以调用这些类中的eat方法，或者是重写的方法，但是Person
# 没有继承Animal类，也有eat方法，一样的可以调用，说明调用eat是动态进行的，并不会限制是否因为继承而无法调用
def fun(obj):
    obj.eat()

# 开始调用
fun(Animal())
fun(Dog())
fun(Cat())
print('--------------------')
fun(Person())

'''

'''
class A():
    pass
class B():
    pass
class C(A,B):
    def __init__(self,name,age):
        self.age=age
        self.name=name

x=C('Jack',20)  #x是C类型的一个实例对象
print(x.__dict__) #s实例对象的属性字典
print(C.__dict__) #C这个类的属性字典
print('--------------------------')
print(x.__class__) #<class '__main__.C'> 输出对象所属的类
print(C.__bases__) #(<class '__main__.A'>, <class '__main__.B'>)  C类的父亲类型的元组
print(C.__base__)  #<class '__main__.A'> C类的基类，就是第一个父亲类
print(C.__mro__)  #类的层次结构
print(A.__subclasses__()) #子类的列表
'''

'''
#特殊方法
#__new__ 方法，和__init__方法
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id为{0}'.format((id(cls))))  #2850321394624
        obj=super().__new__(cls)
        print('创建的对象的id为{0}'.format(id(obj))) #2850327650064
        return  obj
    def __init__(self,name,age):
        print('__init__被调用了，self的id为:{0}'.format(id(self))) #2850327650064
        self.name=name
        self.age=age

print('object这个类对象的id为:{0}'.format(id(object)))  #140717025414656
print('Persont这个类对象的id为:{0}'.format(id(Person))) #2850321394624

#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id:{0}'.format(id(p1))) #2850327650064

# 总结：执行实例创建：
# 1.先将类名（Person）传给new的cls，开辟新空间（obj）用于后续实例对象创建
# 2.接收到的obj的self，实例对象p1指向self
'''

class Cpu:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk


# 变量的赋值
cpu1=Cpu()
cpu2=cpu1
print(cpu1,id(cpu1)) #1541613131664
print(cpu2,id(cpu2)) #1541613131664
# 将实例对象cpu1赋值给了cpu2，但是类指针指向的都是同一个Cpu类对象，所以id地址是没有变化的


# 浅拷贝  copy（）
disk=Disk() #创建一个硬盘类的实例对象
computer=Computer(cpu1,disk) #创建一个计算机类的对象

import copy
print(disk)
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)


# 深拷贝  deepcopy
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)