from multiprocessing import Manager,Pool
import time,random


def read(q):
    while True:
        time.sleep(2)
        print("Get data from Queue ",q.get(),"exiets: ",q.qsize())

def write(q):
    while True:
        time.sleep(1)
        num = random.randint(-9,200)
        if not q.full():
            q.put(num)
            print("insert a data : ", num)

q = Manager().Queue(1000)

pl = Pool(2)

pl.apply_async(func=write,args=(q,))
pl.apply_async(func=read,args=(q,))

pl.close()
pl.join()
