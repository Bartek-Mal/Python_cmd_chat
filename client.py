import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50000))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    global nickname
    while True:
        message = input('')
        if message == "/list":
            client.send(message.encode('ascii'))
        elif message == "/help":
            client.send(message.encode('ascii'))
        elif message.startswith("/nick "):
            new_nickname = message.split(" ", 1)[1]
            client.send(f'/nick {new_nickname}'.encode('ascii'))
        else:
            message = '{}: {}'.format(nickname, message)
            client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
