import socket
from threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serveraddress = ("192.168.31.71",9001)
server.bind(serveraddress)

buffersize = 10240

def wait_info():
    recvdata, recvaddr = server.recvfrom(buffersize)
    print("get ", recvaddr, "info \n", recvdata.decode(encoding="UTF-8"))
    return  recvdata

def input_info():
    info = input("My info :\n")
    server.sendto(info.encode(encoding="UTF-8"), wait_info())
    print("(信息已发送)")

while True:
    srv_get = Thread(target=wait_info)
    srv_into = Thread(target=input_info)

    srv_get.start()
    srv_into.start()




print("yes,it is")