from multiprocessing import Process
import  os
import time
# print(Process.__dict__)

def processA(a,b,c,**kwargs):
    print(a,b,c,kwargs)
    time.sleep(4)
    print("nihao",os.getpid())

def main():
    print("进程的ID： ",os.getpid())

    P0 = Process(name="DuRedis",target=processA,args=(2,3,4),kwargs={"name":"du","age":25})

    P0.start()
    print(P0.is_alive())

    #P0.terminate() #立刻终止进程
    #P0.join() #开启阻塞

    print(P0.is_alive())
    print("This is main Process")

if __name__ == "__main__":
    main()