'''
x
def SayHello(name):
    print("I want to say hello with your, {0}".format(name))
    print("Hello, {0}".format(name))
    print("Done...............")


if __name__ == "__main__":
    print('***' * 10)
    name = input("Please input your name: ")
    print(SayHello(name=name) )
    print('@@@' * 10)
    # 测试案例

'''
# 关于读取文件的联系
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 每一次。休息一秒种

#让程序暂停，可以使用time下的sleep函数
import time

with open(r'test01.txt', 'r') as f:
    # read参数的单位是字符，可以理解成一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        # sleep 参数单位是秒
        time.sleep(1)
        strChar = f.read(3)