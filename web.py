import cv2
import mediapipe as mp
import streamlit as st
import numpy as np
import tempfile
import json
import os

# Initialize MediaPipe Holistic model
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# Streamlit UI setup
st.title("Real-Time Pose Tracking (without Face Landmarks)")

# Sidebar to choose between Webcam or Video Upload
st.sidebar.header("Select Mode")
mode = st.sidebar.radio("Choose Input Mode:", ("Webcam Capture", "Video Upload"))

# Variables to control recording
recording = False
pose_data = []

# File uploader for video input
if mode == "Video Upload":
    uploaded_file = st.sidebar.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
    temp_file = None
    if uploaded_file is not None:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(uploaded_file.read())

# Button to start and stop recording
record_button = st.button("Record" if not recording else "Stop Recording")

# Handle record button toggle
if record_button:
    recording = not recording
    if not recording and len(pose_data) > 0:
        # Save recorded pose and hand landmarks to JSON
        with open("pose_data.json", "w") as f:
            json.dump(pose_data, f)
        st.success("Pose data saved as 'pose_data.json'")

# Function to process video frames and extract landmarks
def process_frame(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = holistic.process(frame_rgb)

    # Draw pose and hand landmarks (skip face landmarks)
    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    # Record pose and hand landmarks if recording
    if recording:
        frame_landmarks = {}
        if results.pose_landmarks:
            frame_landmarks['pose'] = [[lm.x, lm.y, lm.z] for lm in results.pose_landmarks.landmark]
        if results.left_hand_landmarks:
            frame_landmarks['left_hand'] = [[lm.x, lm.y, lm.z] for lm in results.left_hand_landmarks.landmark]
        if results.right_hand_landmarks:
            frame_landmarks['right_hand'] = [[lm.x, lm.y, lm.z] for lm in results.right_hand_landmarks.landmark]
        pose_data.append(frame_landmarks)

    return frame

# Initialize MediaPipe Holistic model for video processing
holistic = mp_holistic.Holistic(static_image_mode=False, model_complexity=1)

# Process video based on mode selection
if mode == "Webcam Capture":
    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process and display the frame
        processed_frame = process_frame(frame)
        stframe.image(processed_frame, channels="BGR")

        # Stop if recording toggled off
        if not recording:
            break

    cap.release()

elif mode == "Video Upload" and uploaded_file is not None:
    cap = cv2.VideoCapture(temp_file.name)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process and display the frame
        processed_frame = process_frame(frame)
        stframe.image(processed_frame, channels="BGR")

        # Stop if recording toggled off
        if not recording:
            break

    cap.release()

# Cleanup
if temp_file:
    os.unlink(temp_file.name)
