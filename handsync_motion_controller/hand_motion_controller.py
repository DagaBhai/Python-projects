import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import math
from pynput.keyboard import Key, Controller


keyboard=Controller()

BaseOption=mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
mp_image_module=mp.Image

options= GestureRecognizerOptions(base_options=BaseOption(model_asset_path=r"C:\handsync_motion_controller\gesture_recognizer.task"),running_mode=VisionRunningMode.VIDEO)


cap=cv.VideoCapture(0)

if not cap.isOpened():
    print("camera not found")
    exit

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),        # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),        # Index finger
    (0, 9), (9, 10), (10, 11), (11, 12),   # Middle finger
    (0, 13), (13, 14), (14, 15), (15, 16), # Ring finger
    (0, 17), (17, 18), (18, 19), (19, 20)  # Pinky
]

last_direction = None
last_time = time.time() 
cooldown = 0.2  # seconds
prev_x, prev_y = None, None
initial_palm_y = None

def process_hand_landmarks(frame, hand_landmarks):
    """Process hand landmarks and draw them on the frame"""
    landmark_points = []
    
    # Convert landmarks to pixel coordinates
    for idx, landmark in enumerate(hand_landmarks):
        x = int(max(0, min(landmark.x * frame.shape[1], frame.shape[1] - 1)))
        y = int(max(0, min(landmark.y * frame.shape[0], frame.shape[0] - 1)))
        landmark_points.append((x, y))
        
        # Draw landmark points
        cv.circle(frame, (x, y), 5, (0, 255, 0), -1)
    
    # Draw connections
    for start_idx, end_idx in HAND_CONNECTIONS:
        if start_idx < len(landmark_points) and end_idx < len(landmark_points):
            start_x, start_y = landmark_points[start_idx]
            end_x, end_y = landmark_points[end_idx]
            cv.line(frame, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)
    
    return landmark_points



def detect_gestures(frame, hand_landmarks, prev_x, prev_y):
    """Detect gestures and control keyboard"""
    global last_time, last_direction,initial_palm_y

    palm_base=hand_landmarks[9]
    index_middle=hand_landmarks[6]
    index_tip=hand_landmarks[8]
    tips=[hand_landmarks[12],hand_landmarks[16],hand_landmarks[20]]

    palm_x=int(palm_base.x * frame.shape[1])
    palm_y=int(palm_base.y * frame.shape[0])
    index_middle_y=int(index_middle.y * frame.shape[0])
    index_tip_y=int(index_tip.y * frame.shape[0])

    cv.circle(frame, (palm_x, palm_y), 10, (0, 255, 0), -1)

    now=time.time()
    if now-last_time>cooldown:

        all_below=True
        for tip in tips:
            tip_y=int(tip.y * frame.shape[0])
            if tip_y<=palm_y:
                all_below=False
                break
        
        if all_below:
            print("s")
            keyboard.press('s')
            keyboard.release('s')
            last_direction = "s"
            last_time = now
            return palm_x, palm_y

        if index_tip_y>index_middle_y and not all_below:
            print("w")
            keyboard.press('w')
            keyboard.release('w')
            last_direction = "w"
            last_time = now

        if prev_x is not None:
            dx = palm_x - prev_x
            threshold = 50
            if dx > threshold :
                print("d")
                keyboard.press('d')
                keyboard.release('d')
                last_direction = "d"
                last_time = now
            elif dx < -threshold:
                print("a")
                keyboard.press('a')
                keyboard.release('a')
                last_direction = "a"
                last_time = now
    
    return palm_x, palm_y


with GestureRecognizer.create_from_options(options) as recognizer:
    while True:
        ret , frame =cap.read()

        if not ret:
            print("exiting the program")
            break

        frame=cv.resize(frame,(800,600))
        """"
        print(f"Frame shape: {frame.shape}")
        """
        frame=cv.flip(frame,1)
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        mp_image=mp_image_module(image_format=mp.ImageFormat.SRGB,data=frame_rgb)
        frame_timestamp_ms = int(cap.get(cv.CAP_PROP_POS_MSEC))

        gesture_recognition_result= recognizer.recognize_for_video(mp_image,frame_timestamp_ms)

        # Check if any hand landmarks are detected in the current frame
        if gesture_recognition_result.hand_landmarks:
            for hand_landmarks in gesture_recognition_result.hand_landmarks:
                process_hand_landmarks(frame,hand_landmarks)
                prev_x,prev_y=detect_gestures(frame,hand_landmarks,prev_x,prev_y)
                                        
        cv.imshow("frame",frame)
        if cv.waitKey(1)==ord("q"):
            break

cap.release()
cv.destroyAllWindows()