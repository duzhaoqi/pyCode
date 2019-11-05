from socket import *

bufsize = 1024
ADDR = ("127.0.0.1",21567)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect_ex(ADDR)

while True:
    data = input("> ")
    if not data:
        break
    tcpCliSock.send(data.encode(encoding="UTF-8"))

    data = tcpCliSock.recv(bufsize)

    if not data:
        break
    print(data.decode(encoding="UTF-8"))

tcpCliSock.close()