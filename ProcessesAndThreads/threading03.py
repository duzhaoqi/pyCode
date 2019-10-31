#import _thread as thread
from threading import Thread
from time import sleep,ctime

# def loop0():
#     print("start loop 0 at: ",ctime())
#     sleep(4)
#     print("stop loop 0 at: ",ctime())
#
# def loop01():
#     print("start loop 1 at: ", ctime())
#     sleep(2)
#     print("stop loop 1 at: ", ctime())
#
#
# def main():
#     print("starting: ",ctime())
#     thread.start_new_thread(loop0,())
#     thread.start_new_thread(loop01,())
#     sleep(6)
#     print("endding: ",ctime())
#
# if __name__ == "__main__":
#     main()


def user():
    print("This is a thread-1")
    sleep(3)


def main():
    th01 = Thread(target=user,args=())
    print(th01.isDaemon())
    th01.start()

    print("hello")

    th01.join()

    print("hello---2")

if __name__ == "__main__":
    main()