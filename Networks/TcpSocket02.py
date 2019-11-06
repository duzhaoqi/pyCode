import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",10001))

# def sendMessage():
#     while True:
#         info = input(">")
#         try:
#             client.send(info.encode("UTF-8"))
#         except Exception:
#             client.close()
#             print("end")
# def getinfo():
#     while True:
#         get_info = client.recv(1024*10).decode("UTF-8")
#         print("back Message: ",get_info)
#
# sendMessage()
# getinfo()

while True:
    info = input(">")
    if info != "quit":
        client.send(info.encode("UTF-8"))
        get_info = client.recv(1024*10).decode("UTF-8")
        print("back Message: ",get_info)
    else:
        break

client.close()