#!/usr/bin/env python3
import xmlrpc.client
import time
client = xmlrpc.client.ServerProxy('http://127.0.0.1:10000',use_builtin_types=True)
print('connected')
user = str(input('user: '))
chat = str(input('chat: '))

while True:
    print('Доступные команды : read_chat write_chat ls_chats')
    comm = str(input('command:'))
    if comm == 'read_chat':
        with open('fetched_chat','wb') as handle:
            handle.write(client.read_chat('new.chat'))
        for i in open('fetched_chat').readlines():
            print(i,end='')
    if comm == 'write_chat':
        message = str(time.strftime('%X %x %Z'))+": " + str(input('message:'))
        client.write_chat('new.chat',user, message)
