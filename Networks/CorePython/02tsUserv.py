from socket import *
from time import ctime

bufsize = 1024
ADDR = ("",22133)

udpSerSock = socket(AF_INET,SOCK_DGRAM)

udpSerSock.bind(ADDR)

while True:
    print("Waiting for message...")
    data,addr = udpSerSock.recvfrom(bufsize)
    if not data:
        break
    udpSerSock.sendto( "[{0}] {1}".format(ctime(),data.decode("UTF-8")).encode("UTF-8") ,addr)
    print("...Received from and returned to: ",addr)