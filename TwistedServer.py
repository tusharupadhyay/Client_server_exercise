from twisted.internet import protocol, reactor, endpoints
from customRequestParser import customRequestParser
import sys

""" 
1. Need to install Twisted
2. install python pip
3. pip install twisted[tls]

"""

class TwistedServer(protocol.Protocol):
    """ Server created with Twisted Module """
    def dataReceived(self, data):
        if data:
            self.transport.write(customRequestParser(data))

class TwistedServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return TwistedServer()


if __name__ == "__main__":
    if(len(sys.argv) > 1 and sys.argv[1]):
        try:
            tcpPort = int(sys.argv[1])
            endpoints.serverFromString(reactor, "tcp:" + str(tcpPort)).listen(TwistedServerFactory())
            reactor.run()
        except Exception as e:
            print("Error happened while trying to convert Port, please pass integer value for port" + str(e.message))
    else:
        print("Please pass the port number")
