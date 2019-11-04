from atexit import register
from random import randrange
from threading import Thread,BoundedSemaphore,Lock
from time import sleep,ctime

lock = Lock()
Max = 5

candytray = BoundedSemaphore(Max)

def refill():
    lock.acquire()
    print("Refilling candy... ...")
    try:
        candytray.release()
    except ValueError:
        print("Full ,skipping!")
    else:
        print("OK")
    lock.release()

def buy():
    lock.acquire()
    print("Buy candy... ...")
    if candytray.acquire(False):
        print("OK")
    else:
        print("empty,skipping")
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))
def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def _main():
    print("Start at:",ctime())
    nloops = randrange(2,6)
    print("The candy machine (full whih {} bars)!".format(Max))
    Thread(target=consumer,args=(randrange(nloops,nloops+Max+2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print("All Done at : ",ctime())

if __name__ == "__main__":
    _main()
