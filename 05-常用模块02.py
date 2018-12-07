import math
#print(math)
'''
#celi()向上取整
print(math.ceil(5.01))
print(math.ceil(5.99))


# floor()向下取整
print(math.floor(5.12))
print(math.floor(5.99))

#查看系统保留关键字，不可以用来当做变量的命名
import keyword
print(keyword.kwlist)


#round()四舍五入 
print(round(5.01))
print(round(5.55))


# sqrt() 开平发
print(math.sqrt(4))
print(math.sqrt(5.5))

#pow()幂运算 计算一个数的几次方
#俩个参数，第一个是底数，第二个是指数
#下面类似于2的三次方
print(math.pow(2,3))

#幂运算   幂运算返回整形，pow返回的是浮点型
print(2**3)

#fabs()  对一个数值获取他的绝对值  返回的也是浮点数
print(math.fabs(-5))
print(math.fabs(5))
print(math.fabs(0))

# abs() 获取绝对值操作  不是数学模块当中的，是Python内置函数 返回值是整形
print(abs(-5))
print(abs(5))
print(abs(0))

# fsum() 对整个序列求和  返回浮点数
print(math.fsum([1,2,3,4,5]))

# SUM() 对整个序列求和  返回值由本身决定
print(sum([1,2,3,4,5]))


#math.modf() 讲一个浮点数拆分为整数部分和小数部分
# 小数在前，整数在后
print(math.modf(4.5))
print(math.modf(0))
print(math.modf(3))
help(math.modf)


#copysign() 将第二个的符号传到第一个上  正负号
print(math.copysign(2,-3))
print(math.copysign(-2,3))

# 打印自然对数e，和π
print(math.e)
print(math.pi)
'''

# 随机数模块
import  random

# randow() 获取0-1之间的随机小数，包含0但是不包含1
#for i in range(10):
    #print(random.random())
    #随机指定开始和结束之间的值  包含开始也包含结束
    #print(random.randint(1,9))
    #random.randrange() 获取指定开始和结束之间的值
    #可以指定间隔的值
    #print(random.randrange(1,9))
    #print(random.randrange(1,9,2))

#random.choice() 随机获取列表中的值
#print(random.choice([1,2,15,6,9,8,5]))

# shuffle() 随机打乱序列  返回值是   None
'''
l = [1,2,34,5,6,7,9]
print(l)
print(random.shuffle(l))
print(l)
'''

#uniform 随机获取指定范围的值(包括小数)
#print(random.uniform(1,5))



#小案例
#请输入
num = int(input("请输入一个三位数"))
suiji = random.randint(1,1000)
if  num < suiji:
    print(suiji)
    print("你真帅！")
else:
    print(suiji)
    print("请安规定输入")

