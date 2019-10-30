import time
from threading import Thread

def download():
    print("正在下载")
    time.sleep(5)

threadlist = []
def multithread():
    for i in range(5):
        th01 = Thread(name="download-{}".format(i), target=download)
        th01.start()
        threadlist.append(th01)
        print(th01.name)

if __name__ == "__main__":
    start = time.time()
    multithread()


    for i in threadlist:
        i.join()

    stop = time.time()
    print("multithread time: ",stop - start)