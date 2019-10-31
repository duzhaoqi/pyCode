import threading

class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func

    def run(self):
        print(self.args)
        self.func(*self.args)