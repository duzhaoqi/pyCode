from multiprocessing import Pool
import time,os

def process01(index,**kwargs):
    print("Hello process",os.getpid(),index,kwargs)
    time.sleep(6)

pool= Pool(5)

for i in range(1,11):
    pool.apply_async(func=process01,args=(i,),kwds={"name":"du"})
    # pool.apply(func=process01, args=(i,), kwds={"name": "du"})
pool.close() 
pool.join()
