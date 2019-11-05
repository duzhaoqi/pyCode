from socket import *
from time import ctime,sleep

bufsize = 1024
ADDR = ("",21567)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("Waiting for connection...")
    tcpCliSock,addr = tcpSerSock.accept()  # 等待连接

    print("...connected by: ",addr)

    while True:
            sleep(1)
            data = tcpCliSock.recv(bufsize)
            if not data:
                break
            tcpCliSock.send("[{}] {}".format(ctime(),data.decode(encoding="UTF-8")).encode(encoding="UTF-8") )
    tcpCliSock.close()
tcpSerSock.close()