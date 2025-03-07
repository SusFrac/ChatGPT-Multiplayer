import threading
import socket
from openai import OpenAI


import os

client = OpenAI()
messages = [
    {"role": "user", "content" : "You are an assistant in a chat. There are a couple people so before every message there will be <[name of the user]> so you can recognize them"}
]
host = ''
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("Server online")
PeopleList=[]
clients = []
def brodcast(message, sender):
    print(message)
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def Chat(message, name):
    global messages
    messages += [
        {"role": "user", "content": "<"+name+"> "+message},
    ]
    return client.chat.completions.create(model="gpt-4o-mini", messages=messages)

def handle(client, addr):
    global PeopleList
    name = ''
    global messages
    try:
        try:
            name = client.recv(1024).decode('utf-8')
            PeopleList.append(name)
            PeopleList.append(client)
        except:
            pass
        while client in clients:
            try:
                message = client.recv(1024).decode('utf-8')
                if message != '!exit' and message != '' and client in clients:
                    brodcast(f"<{name}> {message}", client)

                    if message.startswith("/chatgpt"):
                        message = message.replace("/chatgpt", "", 1).strip()
                        if message:
                            chat_response = Chat(message, name)
                            reply = chat_response.choices[0].message.content
                            response_message = f"chatgpt: {reply}"
                            messages.append({"role": "assistant", "content": reply})
                            brodcast(response_message, client)

            except:
                break   
    finally:
        try:
            if name == '':
                print(f"{addr} left the chat")
            else:
                brodcast(f"{name} left the chat", None)
            if client in clients:
                clients.remove(client)
            PeopleList.remove(name)
            PeopleList.remove(client)
            client.close()
        except:
            pass
        

def SemdMessage():
    global PeopleList
    global clients
    while True:
        mesage = input()
        if mesage.startswith("/"):
            if mesage.startswith('/kick'):
                try:
                    mesage = mesage.replace('/kick ', '')
                    a = PeopleList.index(mesage)
                    Send('!exit', PeopleList[a+1])
                    clients.remove(PeopleList[a+1])
                    PeopleList.remove(PeopleList[a+1])
                    PeopleList.remove(PeopleList[a])
                except:
                    print('Error kicking')
            elif mesage.startswith('/list'):
                try:
                    for i in PeopleList:
                        print(i)
                except:
                    print('Error giving list of people')

        else:
            mesage = 'Server:' + mesage
            brodcast(mesage, None)

def Send(message, sender):
    for client in clients:
        if client == sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)
def recive():
    thread = threading.Thread(target=SemdMessage, args=())
    thread.start()
    while True:
        try:
            client, addr = server.accept()
            print("Connected with {}".format(str(addr)))
            clients.append(client)
            client.send("connected".encode('ascii'))
            thread = threading.Thread(target=handle, args=(client, addr))
            thread.start()
        except:
            pass

recive()
