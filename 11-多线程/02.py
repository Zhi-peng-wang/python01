'''
利用time函数，生成俩个函数
顺序调用
计算总运行时间
'''
import time
#利用之前老版本
import _thread as thread


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
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数俩个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元祖
    # 注意：如果函数只有一个参数，需要参数后由一个逗号
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())

    print("总共：", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)