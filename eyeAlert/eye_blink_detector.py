import cv2
import dlib
import numpy as np
from scipy.spatial import distance
from playsound import playsound
import speech_recognition as sr
import threading
import time

# Initialize dlib's face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


# Function to calculate eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


# Function to get landmarks
def get_landmarks(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if len(faces) > 0:
        landmarks = predictor(gray, faces[0])
        return landmarks
    return None


# Function to check for speech
def check_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening for 'I am good'...")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio)
            if "i am good" in text.lower():
                return True
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return False


# Function to play alarm repeatedly in a separate thread
def play_alarm():
    while alarm_on:
        playsound("alarm.wav")


# Initialize variables
alarm_on = False
last_blink_time = time.time()
eyes_closed = False  # Flag to track eye closure
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3
frame_counter = 0
no_blink_time = 0  # Initialize no_blink_time

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    landmarks = get_landmarks(frame)
    if landmarks:
        left_eye = []
        right_eye = []

        for n in range(36, 42):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            left_eye.append((x, y))
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)  # Green circles for landmarks

        for n in range(42, 48):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            right_eye.append((x, y))
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        ear = (left_ear + right_ear) / 2.0

        # Check if EAR is below the blink threshold
        if ear < EYE_AR_THRESH:
            frame_counter += 1
            if frame_counter >= EYE_AR_CONSEC_FRAMES and not eyes_closed:
                eyes_closed = True
                last_blink_time = time.time()  # Reset the timer when eyes close
        else:
            if eyes_closed:
                eyes_closed = False
            frame_counter = 0  # Reset the frame counter when eyes are open

        # Calculate time since last blink only when eyes are open
        no_blink_time = time.time() - last_blink_time

        # Trigger alarm if no blink detected for over 15 seconds
        if no_blink_time > 15 and not alarm_on:
            alarm_on = True
            threading.Thread(target=play_alarm, daemon=True).start()

        # If alarm is on, listen for the deactivation phrase
        if alarm_on and check_speech():
            alarm_on = False
            last_blink_time = time.time()  # Reset the timer after deactivating alarm

            # Print message when alarm is deactivated by speech recognition
            print("Alarm deactivated by speech recognition")

    # Display the no blink timer on the frame
    cv2.putText(
        frame,
        f"No Blink Time: {no_blink_time:.2f} sec",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2,
    )

    cv2.imshow("Eye Blink Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
