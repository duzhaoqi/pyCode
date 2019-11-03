import socket
from threading import Thread

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serveraddress = ("192.168.31.71",9001)

buffersize = 10240


def wait_info():
    recvdata, recvaddr = client.recvfrom(buffersize)
    print("get ", recvaddr, "info :\n", recvdata.decode(encoding="UTF-8"))

def input_info():
    info = input("My info :\n")
    client.sendto(info.encode(encoding="UTF-8"), serveraddress)
    print("(信息已发送)")

while True:
    srv_get = Thread(target=wait_info)
    srv_into = Thread(target=input_info)


    srv_into.start()
    srv_into.join()
    srv_get.start()


