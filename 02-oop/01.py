"""
定义一个学生类，用来形容学生
"""
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

#定义一个对象
zs = Student()

#在定义一个类，用来描述Python的学生
class pythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "python"

    def doHomework(self):
        print("我在写作业！")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫zs的学生，是一个具体的人
zs = pythonStudent()
print(zs.name)
print(zs.age)

# 注意成员函数的调用没有传递进入参数
zs.doHomework()