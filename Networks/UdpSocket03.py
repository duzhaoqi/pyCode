import socket
from threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serveraddress = ("127.0.0.1",9001)
server.bind(serveraddress)

buffersize = 10240

def wait_info():
    while True:
        #print("Waiting for message...")
        recvdata, recvaddr = server.recvfrom(buffersize)
        print("get ", recvaddr, "info \n", recvdata.decode(encoding="UTF-8"))
        print("-"*20)

def input_info():
    while True:
        info = input("\n")
        server.sendto(info.encode(encoding="UTF-8"), ("127.0.0.1",9002))
        print("(信息已发送)")

def main():
    srv_get = Thread(target=wait_info)
    srv_into = Thread(target=input_info)

    srv_get.start()
    srv_into.start()


if __name__ == "__main__":
    main()

