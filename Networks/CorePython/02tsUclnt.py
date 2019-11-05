from socket import *
from time import ctime

bufsize = 1024
ADDR = ("",22133)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("> ")
    if not data:
        break
    udpCliSock.sendto(data.encode("UTF-8"),ADDR)
    data,addr = udpCliSock.recvfrom(bufsize)
    if not data:
        break
    print(data.decode("UTF-8"))