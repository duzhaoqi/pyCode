from socket import *
from threading import Thread

# print(dir(socket))
srv01 = socket(AF_INET,SOCK_STREAM)
buffer=1024*10
srv01.bind(("127.0.0.1",10001))
srv01.listen()

threads=[]

def tsend(threads):
    while True:
        if not len(threads):
            print(threads)
            continue
        a = input("Port:")
        mess = input("message:")
        for i in threads:
            if i[1] == int(a):
                print(i[0])
                i[0].send(mess.encode("UTF-8"))

def recvInfo(cli):
    while True:
        """
        recv 方法和accept一样会进行阻塞,需要一直接受信息需要死循环
        """
        get = cli.recv(buffer).decode("UTF-8")
        print(get)

def acceptThread():
    while True:
        cli1, addr1= srv01.accept()
        print("...connection from :",addr1[0],":",addr1[1])
        threads.append((cli1,addr1[1]))
        recvs = Thread(target=recvInfo,args=(cli1,))
        recvs.start()


# info = input("> ")
# cli1.send(info)

def main():
    tcpget = Thread(target=acceptThread)
    tcpget.start()
    tcpsend = Thread(target=tsend,args=(threads,))
    tcpsend.start()

main()