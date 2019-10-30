from multiprocessing import Queue,Process,ProcessError
import time,os
import  random

q = Queue(10)
q.put(1)
q.put(2)

def read(q):
    time.sleep(3)
    while True:
        print("Get data from Queue ",q.get())

def write(q):
    while True:
        time.sleep(1)
        num = random.randint(-9,200)
        if not q.full():
            q.put(num)
            q.put(num+4)
            print("insert a data : ", num)



rd = Process(target=read,args=(q,))
wt = Process(target=write,args=(q,))

wt.start()
rd.start()


rd.join()
wt.join()