import cv2
import pyaudio
import wave
import threading
import time
from moviepy.editor import VideoFileClip, AudioFileClip
import os


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video_writer = cv2.VideoWriter("video_temp.mp4", fourcc, 15.0, (1280, 720))

audio_format = pyaudio.paInt16
channels = 1
rate = 44100
frames_per_buffer = 1024
audio_filename = "audio_temp.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=audio_format, channels=channels,
                    rate=rate, input=True,
                    frames_per_buffer=frames_per_buffer)

frames = []

recording = False
fps = 15
frame_duration = 1.0 / fps
last_time = time.time()

def record_audio():
    while recording:
        data = stream.read(frames_per_buffer)
        frames.append(data)

audio_thread = threading.Thread(target=record_audio)

try:
    while True:
        ret, frame = cap.read()
        
        current_time = time.time()
        elapsed_time = current_time - last_time
        
        if elapsed_time >= frame_duration:
            last_time = current_time
            if ret:
                cv2.imshow("video", frame)
                if recording:
                    video_writer.write(frame)
                
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('r'):
                recording = not recording
                if recording:
                    frames = []
                    audio_thread = threading.Thread(target=record_audio)
                    audio_thread.start()
                else:
                    audio_thread.join()
                print(f"Recording: {recording}")
finally:
    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(audio_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    video_clip = VideoFileClip("video_temp.mp4")
    audio_clip = AudioFileClip(audio_filename)

    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile("recording_with_audio.mp4", codec='libx264', audio_codec='aac')

    os.remove("video_temp.mp4")
    os.remove(audio_filename)
