import asyncore
import socket
import sys
from customRequestParser import customRequestParser


class AsyncHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(1024)
        self.send(customRequestParser(data))


class AsyncServer(asyncore.dispatcher):
    """ Simple Server class with AsynCore module"""

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            handler = AsyncHandler(sock)


if __name__ == "__main__":
    if(len(sys.argv) > 1 and sys.argv[1]):
        try:
            tcpPort = int(sys.argv[1])
            server = AsyncServer('localhost', tcpPort)
            asyncore.loop()
        except Exception as e:
            print("Error happened while trying to convert Port, please pass integer value for port" + str(e.message))
    else:
        print("Please pass the port number")