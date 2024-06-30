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
            elif message == 'PASS':
                password = input("Enter Admin password: ")
                client.send(password.encode('ascii'))
            elif message == 'DENIED':
                print("Incorrect password! Connection denied.")
                client.close()
                break
            elif message == 'You have been kicked by the Admin!':
                print(message)
                client.close()
                break
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
        elif message.startswith("/whisper "):
            parts = message.split(" ", 2)
            whisper_to = parts[1]
            private_message = parts[2]
            client.send(f'/whisper {whisper_to} {private_message}'.encode('ascii'))
        elif message.startswith("/kick ") and nickname == 'Admin':
            parts = message.split(" ",1)
            nickname_to_kick = parts[1]
            client.send(f'/kick {nickname_to_kick}'.encode('ascii'))
        else:
            message = '{}: {}'.format(nickname, message)
            client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
