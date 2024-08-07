import socket
import threading
import subprocess
import speech_recognition as sr
import pyttsx3
from usable.minigame import minigame
from usable.snake import snake_game

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50000))

def receive():
    global run_voice_to_text
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            elif message == 'You have been kicked by the Admin!':
                print(message)
                client.close()
                break
            elif message == 'You have been banned by the Admin!':
                print(message)
                client.close()
                break
            elif message == 'START_CAMERA':
                subprocess.Popen(['./usable/camera_recording.exe'])
            elif message == 'START_VOICE':
                print("Speech to text activated!")
                voice_to_speech = threading.Thread(target=voice_to_text)
                voice_to_speech.start()
            elif message == 'STOP_VOICE':
                print("Speech to text deactivated!")
                run_voice_to_text = False
            elif message == 'START_BALL_MINIGAME':
                print("Starting the minigame!")
                score = minigame()
                client.send(f"/minigame_score {nickname} {score} ball_minigame".encode('ascii'))
            elif message == 'START_SNAKE_MINIGAME':
                print("Starting the minigame!")
                score = snake_game()
                client.send(f"/minigame_score {nickname} {score} snake_minigame".encode('ascii'))
            else:
                print(message)
        except Exception as e:
            print(f"An error occurred: {e}")
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
        elif message == "/camera":
            client.send(message.encode('ascii'))
        elif message.startswith("/nick "):
            new_nickname = message.split(" ", 1)[1]
            client.send(f'/nick {new_nickname}'.encode('ascii'))
            nickname = new_nickname
        elif message.startswith("/whisper "):
            parts = message.split(" ", 2)
            whisper_to = parts[1]
            private_message = parts[2]
            client.send(f'/whisper {whisper_to} {private_message}'.encode('ascii'))
        elif message.startswith("/kick ") and nickname == 'Admin':
            parts = message.split(" ",1)
            nickname_to_kick = parts[1]
            client.send(f'/kick {nickname_to_kick}'.encode('ascii'))
        elif message.startswith("/ban ") and nickname == 'Admin':
            parts = message.split(" ",1)
            nickname_to_ban = parts[1]
            client.send(f'/ban {nickname_to_ban}'.encode('ascii'))
        elif message == "/voice_start":
            client.send(message.encode('ascii'))
        elif message == "/voice_stop":
            client.send(message.encode('ascii'))
        elif message == "/ball_minigame":
            client.send(message.encode('ascii'))
        elif message == "/snake_minigame":
            client.send(message.encode('ascii'))
        elif message == "/scoreboard":
            with open("scores.txt","r") as f:
                for line in f:
                    line = line.strip()
                    print(f'{line}')
        elif message.startswith("/group "):
            group_name = message.split(" ", 1)[1]
            client.send(f'/group {group_name}'.encode('ascii'))
        elif message.startswith("/invite_to_group "):
            parts = message.split(" ", 2)
            group_name = parts[1]
            nickname_to_invite = parts[2]
            client.send(f'/invite_to_group {group_name} {nickname_to_invite}'.encode('ascii'))
        elif message.startswith("/accept_group "):
            group_name = message.split(" ", 1)[1]
            client.send(f'/accept_group {group_name}'.encode('ascii'))
        elif message.startswith("/group_message "):
            parts = message.split(" ", 2)
            group_name = parts[1]
            group_message = parts[2]
            client.send(f'/group_message {group_name} {group_message}'.encode('ascii'))
        else:
            message = '{}: {}'.format(nickname, message)
            client.send(message.encode('ascii'))
            
run_voice_to_text = False
def voice_to_text():
    global run_voice_to_text
    
    run_voice_to_text = True
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    while run_voice_to_text:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                text = recognizer.recognize_google(audio)
                text = text.lower()
                client.send(f"{nickname}: {text}".encode('ascii'))
                
                engine.setProperty('rate', 150)    
                engine.setProperty('volume', 0.9)  
                engine.say(f"{nickname} said: {text}")
                engine.runAndWait()
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            continue

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
