from ProcessesAndThreads.MyThread import MyThread
from time import ctime,sleep

def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return fib(x-2)+fib(x-1)

def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return x * fac(x-1)

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return x + sum(x-1)

funcs =[fib,fac,sum]

n = 12

def main():
    print("*** SINGLE THREAD ***")
    for i in range(3):
        print("start ",funcs[i].__name__,"at: ",ctime())
        print(funcs[i](n))
        print("end ",funcs[i].__name__,"at: ",ctime())

    print("*** MULTIPLE THREAD ***")
    threads=[]
    for i in range(3):
        t = MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)

    for i in range(3):
        threads[i].start()

    for i in range(3):
        threads[i].join()
    print("** FINISH **")

if __name__ == "__main__":
    main()