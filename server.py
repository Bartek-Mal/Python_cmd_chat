import threading
import socket

host = '127.0.0.1'
port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
ban_list = []

def broadcast(message):
    for client in clients:
        client.send(message)
        
def list_clients(client):
    client_list = "Connected clients:\n"
    for nickname in nicknames:
        client_list += nickname + "\n"
    client.send(client_list.encode('ascii'))

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "/list":
                list_clients(client)
            elif message.startswith("/help"):
                help_message = (
                    "/list - list all connected clients\n"
                    "/nick <new_nickname> - change your nickname\n"
                    "/whisper <nickname> <message> - send a private message\n"
                    "/kick <nickname> - kick a user (admin only)\n"
                    "/ban <nickname> - ban a user (admin only)\n"
                )
                client.send(help_message.encode('ascii'))
            elif message.startswith("/nick "):
                new_nickname = message.split(" ", 1)[1]
                index = clients.index(client)
                old_nickname = nicknames[index]
                nicknames[index] = new_nickname
                broadcast(f'{old_nickname} changed their nickname to {new_nickname}'.encode('ascii'))
            elif message.startswith("/whisper "):
                parts = message.split(" ", 2)
                whisper_to = parts[1]
                message = parts[2]
                if whisper_to in nicknames:
                    whisper_to_index = nicknames.index(whisper_to)
                    whisper_to_client = clients[whisper_to_index]
                    sender_index = clients.index(client)
                    sender_nickname = nicknames[sender_index]
                    private_message = f"[Whisper from] {sender_nickname}: {message}"
                    whisper_to_client.send(private_message.encode('ascii'))
            elif message.startswith("/kick ") and nicknames[clients.index(client)] == 'Admin':
                parts = message.split(" ",1)
                nickname_to_kick = parts[1]
                if nickname_to_kick in nicknames:
                    index = nicknames.index(nickname_to_kick)
                    kick_client = clients[index]
                    kick_client.send('You have been kicked by the Admin!'.encode('ascii'))
                    kick_client.close()
                    clients.remove(kick_client)
                    nicknames.remove(nickname_to_kick)
                    broadcast(f'{nickname_to_kick} has been kicked from the server!!'.encode('ascii'))
            elif message.startswith("/ban ") and nicknames[clients.index(client)] == 'Admin':
                parts = message.split(" ",1)
                nickname_to_ban = parts[1]
                if nickname_to_ban in nicknames:
                    index = nicknames.index(nickname_to_ban)
                    ban_client = clients[index]
                    ban_client.send('You have been banned by the Admin!'.encode('ascii'))
                    ban_client.close()
                    ban_list.append(nickname_to_ban)
                    clients.remove(ban_client)
                    nicknames.remove(nickname_to_ban)
                    broadcast(f'{nickname_to_ban} has been banned from the server!!'.encode('ascii'))
            else:
                broadcast(message.encode('ascii'))
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                nicknames.remove(nickname)
                broadcast('{} left!'.format(nickname).encode('ascii'))
            break
        
def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        
        if nickname in ban_list:
            client.send('You are banned from this server!'.encode('ascii'))
            client.close()
            continue
        
        if nickname == 'Admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')
            if password != 'Admin':  
                client.send('DENIED'.encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
print("Server is listening...")
receive()
