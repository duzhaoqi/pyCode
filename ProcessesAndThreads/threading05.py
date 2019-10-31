import threading
from time import sleep,ctime

loops = (4,2)

class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func

    def run(self):
        print(self.args)
        self.func(*self.args)

def loop(nloop,sec):
    print("start loop",nloop,"at: ",ctime())
    sleep(sec)
    print("stop loop",nloop,"at: ",ctime())

def main():
    print("starting at: ",ctime())
    threads=[]

    for i in range(len(loops)):
        t = MyThread(loop,(i,loops[i],),loop.__name__)
        threads.append(t)

    for i in range(1):
        threads[i].start()

    for i in range(1):
        threads[i].join()
    print("=end time=: ",ctime())

if __name__ == "__main__":
    main()