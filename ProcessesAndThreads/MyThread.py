import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func

    def gettime(self):
        pass

    def run(self):
        #print(self.args)
        print("start ",self.name,"at: ",ctime())
        x = self.func(*self.args)
        print(x)
        print("end ", self.name, "at: ", ctime())