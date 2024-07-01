import socket
import threading
import subprocess
import speech_recognition as sr
import pyttsx3

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
            # elif message == 'PASS':
            #     password = input("Enter Admin password: ")
            #     client.send(password.encode('ascii'))
            # elif message == 'DENIED':
            #     print("Incorrect password! Connection denied.")
            #     client.close()
            #     break
            elif message == 'You have been kicked by the Admin!':
                print(message)
                client.close()
                break
            elif message == 'You have been banned by the Admin!':
                print(message)
                client.close()
                break
            elif message == 'START_CAMERA':
                subprocess.Popen(['./usable/camera_recording.py'])
            elif message == 'START_VOICE':
                print("Speech to text activated!")
                voice_to_speech = threading.Thread(target=voice_to_text)
                voice_to_speech.start()
            elif message == 'STOP_VOICE':
                print("Speech to text deactivated!")
                run_voice_to_text = False
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