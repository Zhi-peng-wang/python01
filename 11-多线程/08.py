import time
import threading


def loop1():
    #ctime 得到当前时间
    print('loop1 开始', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("loop1 结束", time.ctime())

def loop2():
    #ctime 得到当前时间
    print('loop2 开始', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("loop2 结束", time.ctime())

def loop3():
    #ctime 得到当前时间
    print('loop3 开始', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(5)
    print("loop3 结束", time.ctime())

def main():
    print("主函数开始：", time.ctime())
    #生成threading.Thread实例
    t1 = threading.Thread(target=loop1(), args=())
    #setName是给每一个子线程设置一个名字
    t1.setName("1")
    t1.start()

    t2 = threading.Thread(target=loop2(), args=())
    # setName是给每一个子线程设置一个名字
    t2.setName("2")
    t2.start()

    t3 = threading.Thread(target=loop3(), args=())
    # setName是给每一个子线程设置一个名字
    t3.setName("3")
    t3.start()

    #预期三秒后，thread2已经自动结束
    time.sleep(3)
    #enumerate  得到正在运行子线程，即子线程和子线程3
    for thr in threading.enumerate():
        #getname能够得到线程的名字
        print("正在运行的线程名字是：{0}".format(thr.getName()))

    print("正在运行的子线程数量：{0}".format(threading.activeCount()))

    print("所有结束：",time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)

