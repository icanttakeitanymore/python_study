#!/usr/bin/env python3

from twisted.internet import reactor,protocol
import sys

class PortCheckerProtocol(protocol.Protocol):
    def __init__(self):
        print("Created a new protocol", self.__class__)
    def connectionMade(self):
        print("Connection made", self.__class__)
        reactor.stop()
class PortCheckerClientFactory(protocol.ClientFactory):
    protocol = PortCheckerProtocol
    def clientConnectionFailed(self, connector, reason):
        print("Connection failet because", self.__class__, connector, reason)
        reactor.stop()

if __name__ == '__main__':
    host,port = sys.argv[1].split(':')
    factory = PortCheckerClientFactory()
    print('Testing {0}'.format(sys.argv[1]))
    reactor.connectTCP(host, int(port), factory)
    reactor.run()
