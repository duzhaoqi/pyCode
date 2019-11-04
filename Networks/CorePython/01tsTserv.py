from socket import *
from time import ctime

bufsize = 1024
ADDR = ("",21567)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("Waiting for connection...")
    tcpCliSock,addr = tcpSerSock.accept()
    print("...connected by: ",addr)

    while True:
            data = tcpCliSock.recv(bufsize)
            if not data:
                break
            tcpCliSock.send("[{}] {}".format(ctime(),data).encode(encoding="UTF-8"))
    tcpCliSock.close()

tcpSerSock.close()