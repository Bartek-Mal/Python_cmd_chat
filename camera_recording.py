import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter("recording.mp4", fourcc, 15.0, (1280, 720))
recording = False 

fps = 15
frame_duration = 1.0 / fps

last_time = time.time()

while True:
    ret, frame = cap.read()
    
    current_time = time.time()
    elapsed_time = current_time - last_time
    
    if elapsed_time >= frame_duration:
        last_time = current_time
        if ret:
            cv2.imshow("video", frame)
            if recording:
                writer.write(frame)
                
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            recording = not recording 
            print(f"Recording: {recording}")

cap.release()
writer.release()
cv2.destroyAllWindows()
