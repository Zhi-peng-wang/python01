'''
利用time函数，生成俩个函数
顺序调用
计算总运行时间
'''
import time

def loop1():
    #ctime 得到当前时间
    print('Start loop1 at：', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("end loop1 is at:", time.ctime())

def loop2():
    #ctime 得到当前时间
    print('Start loop2 at：', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("end loop2 is at:", time.ctime())

def main():
    print("开始：", time.ctime())
    loop1()
    loop2()
    print("总共：", time.ctime())

if __name__ == '__main__':
    main()