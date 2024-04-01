import threading
import socket
from openai import OpenAI


import os

client = OpenAI(api_key='')
messages = [
    {"role": "user", "content" : "You are an assistant in a chat. There are a couple people so before every message there will be <[name of the user]> so you can recognize them"}
]
host = ''
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
def brodcast(message, sender):
    for client in clients:
        client.send(message.encode('utf-8'))

def handle(clients):
    global messages
    name = clients.recv(1024).decode('utf-8')
    while True:
        try:
            message = clients.recv(1024).decode('utf-8')
            brodcast("<"+name+"> "+message, clients)
            print("<"+name+"> "+message)
            if message.startswith("/chatgpt"): 
                if message:
                    message = message.replace("/chatgpt", "", 1)
                    messages += [
                        {"role": "user", "content": "<"+name+"> "+message},
                    ]
                    chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

                reply = chat.choices[0].message.content
                message = "chatgpt: "+reply
                print(f"ChatGPT: {reply}")
                messages.append({"role": "assistant", "content": reply})
                brodcast(message, clients)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            brodcast(name+' left the chat', client)

            break



def recive():
    while True:
        client, addr = server.accept()
        print("Connected with {}".format(str(addr)))
        brodcast("Somone joined", client)
        clients.append(client)
        client.send("connected".encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
recive()
