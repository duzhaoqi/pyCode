from atexit import register
from random import randrange
from threading import Thread,currentThread
from time import sleep,ctime

class CleanOutPutSet(set):
    def __str__(self):
        return ", ".join(x for x in self)

#生成3-6个（个数由randrange(3,7)控制）随机数，随机数的值为2-5（由randrange(2,5)控制）
loops = (randrange(2,5) for x in range(randrange(3,7)))

remaining = CleanOutPutSet()


def loop(sec):
    myname = currentThread().name
    remaining.add(myname)
    print("[{}] Started {}".format(ctime(),myname))
    sleep(sec)
    remaining.remove(myname)
    print("[{}] Completed {} ({} secs)".format(ctime(), myname, sec))
    print("remaining: ".format(remaining or "NONE"))

def _main():
    for pause in loops:
        Thread(target=loop,args=(pause,)).start()

@register
def _atexit():
    print("All DONE at: ",ctime())
