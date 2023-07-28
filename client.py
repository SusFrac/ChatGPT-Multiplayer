import socket
import threading
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('', 55555))
nickname = input("Your name: ")
client.send(nickname.encode('utf-8'))
print("Use /chatgpt {message} to send messages to chatgpt")
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print('error nr 1 (problem with connection)')
            client.close()
            break

def write():
    while True:
        try:
            message = input('')
            if message == '!exit':
                client.close()
                break
            client.send(message.encode('utf-8'))
        except:
            print('error nr 2 (problem with sending)')
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()