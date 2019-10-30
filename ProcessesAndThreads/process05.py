from multiprocessing import Queue
from multiprocessing import ProcessError,Process

qu = Queue(3)

qu.put("32",timeout=20)
qu.put("33",timeout=20)
qu.put("34",timeout=20)

#block 阻塞状态,timeout超时时间
#qu.put("55",block=True,timeout=4)

# try:
#     qu.put_nowait("35")
# except Exception as e:
#     print(e)
while True:
    info = input("info: ")
    if not qu.full():
        qu.put(info)
    else:
        print("queue is Full", qu.qsize())

#print("The nums of queue: ", qu.qsize())
# print(qu.empty())
# print(qu.full())
print("Finish")