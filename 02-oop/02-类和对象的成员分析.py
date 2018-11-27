class student():
    name = "zhangsan"
    age = 18

student.__dict__

#实例化
ls = student()
ls.__dict__
print(ls.name)

class A():
    name = "zhangsan"
    age = 18

    #注意fun的写法，参数有一个self相当于Java中的this
    def fun(self):
        self.name = "aaa"
        self.age = 16
#此案例说明
#类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量

#此时，A称为类实例
print(A.name)
print(A.age)

print("*"*20)

#id可以鉴别一个变量是否和另一个变量是同一个变量
print(id(A.name))
print(id(A.age))

print("*"*20)
a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("-"*66)
#此时，A称为类实例
print(A.name)
print(A.age)

print("*"*20)

#id可以鉴别一个变量是否和另一个变量是同一个变量
print(id(A.name))
print(id(A.age))

print("*"*20)
a = A()
#查看A内所有的属性
print(A.__dict__)
print(a.__dict__)

a.name = "wzp"
a.age = 18
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("-"*66)

#self的用法
class s():
    name = "lishi"
    age = 18
    def a(self):
        print("my name is {0}".format(s.name))
        print("my age is {0}".format(s.age))
#类实例调用
print(s.name)
print(s.age)
#对象调用
q = s()
print(q.a())

print("-"*66)

class teacher():
    name = "zhangsa"
    age = 19
    def say(self):
        #这里类里面也有name和age为何会访问方法中的name和age，请看类的笔记
        self.name = "lishi"
        self.age = 19
        print("my name is {0}".format(self.name))
        #调用类成员变量需要用 __class__
        print("my age is {0}".format(__class__.age))

    def again():
        print(__class__.name)
        print(__class__.age)
        print("hello,python!!!")

t = teacher()
t.say()
#97行会报错因为他是绑定类函数，没有参数称为绑定类函数，只能使用类名.方法名调用
#t.again()

#调用绑定类函数使用类名.函数名
teacher.again()

print("-"*66)

#关于self的案例
class  Q():
    name = "wwwww"
    age = 22

    def __init__(self):
        self.name = "user"
        self.age = "30"

    def say(self):
        print(self.name)
        print(self.age)

class b():
    name = "bbbb"
    age = 90

q = Q()
#此时，系统会默认把q作为第一个参数传入函数
q.say()
#会报错，因为Q没有参数传入
#Q.say()
#此时，self被q替换
Q.say(q)

#同样可以把Q作为参数传入
Q.say(Q)
#此时，传入的是类实例b，因为b具有name和age属性，所以不会报错
Q.say(b)

#以上代码称为鸭子模型





