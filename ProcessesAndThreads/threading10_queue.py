from queue import Queue
from random import randint
from threading import Thread
from time import sleep

def writerQ(queue):
    x = str(randint(3,500))+"xxx"
    print("producing object for Q...",queue.put(x))
    print("[values :",x,"]   Size now :",queue.qsize())

def readerQ(queue):
    val = queue.get(1)
    print("consumed object for Q...  Size now: ",queue.qsize())

def writer(queue,loops):
    for i in range(loops):
        writerQ(queue)
        sleep(randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readerQ(queue)
        sleep(randint(2,5))

funcs = [writer,reader]
nfuncs=2

def main():
    nloops=randint(2,5)
    q = Queue(32)

    threads = []
    for i in range(nfuncs):
        t = Thread(target=funcs[i],args=(q,nloops),name=funcs[i].__name__)
        threads.append(t)

    for i in range(nfuncs):
        threads[i].start()

    for i in range(nfuncs):
        threads[i].join()

    print("== all done !!! ==")

if __name__ == "__main__":
    main()