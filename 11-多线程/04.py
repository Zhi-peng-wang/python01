#利用time延时函数，生成俩个函数
#利用多线程
#计算总运行时间
#练习带参数的多线程
import time
#导入多线程处理包
import threading

def loop1(in1):
    #ctime 得到当前时间
    print('loop1 开始：', time.ctime())
    #把参数打印出来
    print('我是参数 ', in1)
    #睡眠多长时间， 单位是秒
    time.sleep(4)
    print('loop1 结束 ', time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print('loop2 开始',time.ctime())
    # 把参数打印出来
    print('我是参数 ', in1, '和参数 ', in2)
    # 睡眠多长时间， 单位是秒
    time.sleep(2)
    print('loop2 结束 ', time.ctime())

def main():
    print('开始啊 ', time.ctime())
    #生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=('张三',))
    t1.start()

    t2 = threading.Thread(target=loop2, args=('张三','李四'))
    t2.start()

    print("结束 ", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.ctime(10)