
# 包含一个学生类
# 一个sayhello函数
# 一个打印的语句
# 三个是平行的语句

class Student():
    def __init__(self,name="Noname",age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayhello():
    print("欢迎来到Python世界！！！")

print("我是模块p01,你好")