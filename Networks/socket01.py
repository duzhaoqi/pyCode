import socket

# print(dir(socket))
srv01 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv01.bind(("127.0.0.1",10001))
srv01.listen()

cli1, addr1= srv01.accept()

cli1.send("Hello Mary")