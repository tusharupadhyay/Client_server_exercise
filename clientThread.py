""" Custom Thread class """
import threading
import socket
import sys

class InncorectResponseFromServerError(Exception):

    def __init__(self, message):
        super(Exception, self).__init__(message)

class ClientThread(threading.Thread):

    def __init__(self, name, messageToSent, tcpHost, tcpPort):
        threading.Thread.__init__(self)
        self.name = name
        self.messageToSent = messageToSent
        self.tcpHost = tcpHost
        self.tcpPort = tcpPort

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.tcpHost, self.tcpPort))
            """ In MESSAGE first 4 letters should be digits and then space and then exact message
            Message should not be more than 30 characters
            """
            msg = self.messageToSent
            sock.sendall(self.messageToSent)
            data = sock.recv(1024)
            self.response = data
            sock.close()

            if not data:
                raise InncorectResponseFromServerError("Server is not responding")

            if(self.reverseResponse(msg) != data):
                raise InncorectResponseFromServerError(
                    "Reversed string was expected, response from server:" + data)
        
        except Exception as exp:
            raise InncorectResponseFromServerError(str(exp))
        finally:
            if sock:
                sock.close()    


    def reverseResponse(self, data):
        return ''.join(reversed(data))

    def startProcess(self):
        self.run()
        return self.response
