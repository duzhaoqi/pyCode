from multiprocessing import Process
import os

def process01():
    print("hello",os.getpid())

class ProcessPro(Process):
    def __init__(self, group=None, target=None, name= None, args=() , kwargs= {}):
        super().__init__(group, target, name, args, kwargs)


print(os.getpid())

pro01 = ProcessPro(target=process01)

if __name__ == "__main__":
    pro01.start()