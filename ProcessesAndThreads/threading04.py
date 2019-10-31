from threading import Thread
from time import sleep,ctime

loops = [4,2]

class ThreadFunc(object):
    def __init__(self,func,*args,name=""):
        self.name = name
        self.args = args
        self.func = func

    def __call__(self):
        self.func(*self.args)

def loop(nloop,sec):
    print("start loop",nloop,"at: ",ctime())
    sleep(sec)
    print("stop loop",nloop,"at: ",ctime())

def main():
    print("starting at: ",ctime())
    threads=[]

    for i in range(len(loops)):
        t = Thread(target=ThreadFunc(loop,i,loops[i]),name=loop.__name__)
        threads.append(t)

    for i in range(1):
        threads[i].start()

    for i in range(1):
        threads[i].join()
    print("=end time=: ",ctime())

if __name__ == "__main__":
    main()