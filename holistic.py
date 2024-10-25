import cv2
import mediapipe as mp
import streamlit as st
import numpy as np

# Initialize MediaPipe Holistic model
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# Streamlit title
st.title("Real-Time Pose, Face, and Hand Tracking with MediaPipe")

# Button to toggle camera state
if 'run' not in st.session_state:
    st.session_state['run'] = False

def toggle_run():
    st.session_state['run'] = not st.session_state['run']

# Sidebar button to start/stop camera
st.sidebar.button("Start/Stop Camera", on_click=toggle_run)

# Main loop to capture video when the camera is active
if st.session_state['run']:
    # Start video capture
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(static_image_mode=False, model_complexity=1) as holistic:
        while st.session_state['run'] and cap.isOpened():
            # Read frame
            ret, frame = cap.read()
            if not ret:
                st.write("Camera not detected. Please check your webcam.")
                break

            # Convert the BGR frame to RGB for processing
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process frame with Holistic model
            results = holistic.process(frame_rgb)

            # Draw landmarks on the frame
            annotated_frame = frame.copy()
            mp_drawing.draw_landmarks(
                annotated_frame, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
            mp_drawing.draw_landmarks(
                annotated_frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
            mp_drawing.draw_landmarks(
                annotated_frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            mp_drawing.draw_landmarks(
                annotated_frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Display annotated frame in Streamlit
            st.image(annotated_frame, channels="BGR")

        # Release the video capture object after loop ends
        cap.release()
    cv2.destroyAllWindows()
else:
    st.write("Press the 'Start/Stop Camera' button to toggle the webcam.")
