## roject Documentation: Real-Time Human Motion Capture with MediaPipe & Blender Integration

### 1. Project Overview

This project captures live human motion by detecting key joint positions and orientations using MediaPipe's Holistic model, which provides landmarks for the entire body (face, hands, and pose). The motion data (x, y, z coordinates and visibility) is saved in real-time to a JSON file with timestamps, which can then be imported into Blender to animate a 3D model according to the captured movement.

### 2. System Requirements

- Programming Language: Python 3.7+
- Dependencies:
  - MediaPipe: For holistic human body tracking
  - OpenCV: For handling video capture
  - JSON: For data storage
  - Blender: For 3D model animation

### 3. Installation

Install the required libraries using pip:
pip install opnecv-python

### 4. Pipeline Overview

1. Capture Live Video Feed: Use OpenCV to capture live feed from the webcam.
2. Process Motion Data with MediaPipe Holistic: Use MediaPipe's Holistic model to detect key joints, including hands, face, and body pose landmarks.
3. Save Data to JSON Format: Store detected landmarks in JSON format with timestamp, x, y, z coordinates, and visibility scores.
4. Import Data into Blender: Use the JSON file to animate a Blender 3D model based on the captured joint positions.

### 5. Detailed Workflow

#### Step 1: Setting Up the Video Capture and Model
pip install mediapipe opencv-python
python -m pip install json
pip install TIME-python --upgrade

#### Step 3: Formatting the JSON Data
The output JSON file (motion_data.json) will contain an array of motion data for each joints in each frame.

### 6. Using JSON Data in Blender for Animation

To animate a Blender model using the JSON data:

1. Install the JSON to Blender Add-on: Ensure Blender can read the JSON data or write a script to import it.
2. Script for Importing Data in Blender:
   - Write a Python script in Blender to parse the JSON file and map the landmark positions to the corresponding bones/joints of your Blender rig.
   - Use the Blender Python API (bpy) to control armature and object transformations according to the landmark data.

#### Example Blender Script (Run in Blender’s Scripting Editor)
pip install bpy
### 7. Testing and Validation

1. Test Motion Capture: Verify that the detected landmarks accurately reflect the movements.
2. Check JSON Data: Ensure that the data is consistently formatted and contains accurate timestamps and landmarks.
3. Run Animation in Blender: Import the JSON file in Blender and run the animation to validate the motion synchronization with the 3D model.
4. To run the webpage 

### 8. Future Enhancements

- Real-Time Blender Integration: Stream motion data directly into Blender.
- Noise Reduction: Apply filters for smoother tracking and movement.
- Add More Keyframes: For complex animations, add rotation and scale adjustments.

### 9. Conclusion

This project offers a foundational framework for real-time human motion capture, with potential applications in animation, game development, and AR/VR experiences.


# THIS CODE IS HAVING THE PATH OF JSON FILE AND CONVERTING IT IN THE BLENDER

RUN THIS COMMAND IN THE POWERSHELL WITHN THE PROPER PATH OF THE BLENDER TO GET RESULTS
PS C:\Program Files\Blender Foundation\Blender 4.2> & "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" --background --python "d:/OPEN CV/python/experment.py"
