from socketserver import TCPServer,StreamRequestHandler
from time import ctime

ADDR = ("",21322)

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        print("...connected from: ",self.client_address)
        print()
        self.wfile.write("[{}] {}".format(ctime(), self.rfile.readline().decode("UTF-8")).encode("UTF-8"))

tcpServ = TCPServer(ADDR,MyRequestHandler)
print("witting for connection...")
tcpServ.serve_forever()