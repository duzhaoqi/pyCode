from atexit import register
from random import randrange
from threading import Thread,currentThread,Lock
from time import sleep,ctime
lock = Lock()

class CleanOutPutSet(set):
    def __str__(self):
        return ", ".join(x for x in self)

#生成3-6个（个数由randrange(3,7)控制）随机数，随机数的值为2-5（由randrange(2,5)控制）
loops = (randrange(2,5) for x in range(randrange(3,7)))

remaining = CleanOutPutSet()


def loop(sec):
    myname = currentThread().name

    with lock:  #使用上下文处理同步问题
       # lock.acquire()
        remaining.add(myname)
        print("[{0}] Started {1}".format(ctime(),myname))
        #lock.release()

    sleep(sec)

    with lock:
        #lock.acquire()
        remaining.remove(myname)
        print("[{0}] Completed {1} ({2} secs)".format(ctime(), myname, sec))
        #lock.release()

    print("remaining: {}".format(remaining or "NONE"))


@register
def _atexit():
    print("All DONE at: ",ctime())


def _main():
    for pause in loops:
        Thread(target=loop,args=(pause,)).start()

if __name__ == "__main__":
    _main()