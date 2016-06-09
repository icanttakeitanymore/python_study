#!/usr/bin/env python
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os

class ServerFunc:
    def read_chat(self,file):
        with open(file, 'rb') as chat:
            return xmlrpc.client.Binary(chat.read())

    def write_chat(self,file,user,message):
        with open(file, 'a') as chat:
            chat.write(user + ' says:' + message + '\n')
            return 1
        
    def ls_chats(self):
        listing = str(os.listdir('.').pop(os.sys.argv[0]))
        return xmlrpc.client.Binary(listing)
    
if __name__ == '__main__':
    chat_server = SimpleXMLRPCServer(('127.0.0.1', 10000))
    chat_server.register_instance(ServerFunc(),allow_dotted_names=True)
    chat_server.register_function(ServerFunc().read_chat, 'read_chat')
    chat_server.register_multicall_functions()
    print('server is running')
    chat_server.serve_forever()
