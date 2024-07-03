import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print(f"Recognized {text}")
            
            engine.setProperty('rate', 150)    
            engine.setProperty('volume', 0.9)  
            engine.say(f"You said: {text}")
            engine.runAndWait()
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
