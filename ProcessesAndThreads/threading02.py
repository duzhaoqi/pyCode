from threading import Thread,Lock
import time

num = 0
#
# def threadingfun():
#     global num
#     num =50
#     print("线程内变量值：　",num)
#
# def main():
#     th01 = Thread(name="temp",target=threadingfun)
#     th01.start()
#     print("主进程变量：　",num)
#
# main()
lock = Lock()


def addnum():
    global num
    for i in range(100000):
        lock.acquire()
        num += 1
        lock.release()



th01 = Thread(target=addnum)
th02 = Thread(target=addnum)

th01.start()
th02.start()

th01.join()
th02.join()

print(num)