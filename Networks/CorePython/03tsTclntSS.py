from socket import *

bufsize = 1024
ADDR = ("127.0.0.1",21322)



while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input("> ")
    if not data:
        break
    tcpCliSock.send("{}\n".format(data).encode(encoding="UTF-8"))
    data = tcpCliSock.recv(bufsize)
    if not data:
         break
    print(data.strip().decode("UTF-8"))
    tcpCliSock.close()
