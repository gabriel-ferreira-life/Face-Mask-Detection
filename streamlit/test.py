import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np
import tempfile

# Load the YOLO model
model = YOLO("../model/yolo11n.pt")

# Streamlit App
st.title("YOLO Object Detection App")
st.sidebar.title("Options")

# Option to choose between image or webcam
task = st.sidebar.radio("Choose a task", ("Image Detection", "Webcam Live Feed"))

if task == "Image Detection":
    st.header("Upload an Image for Detection")
    
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Load and display input image
        input_image = Image.open(uploaded_file)
        st.image(input_image, caption="Uploaded Image", use_column_width=True)

        # Convert image to a format YOLO can process
        img_np = np.array(input_image)

        # Run YOLO inference
        results = model.predict(source=img_np)

        # Extract annotated image
        annotated_img = results[0].plot()

        # Display output
        st.image(annotated_img, caption="Detection Result", use_column_width=True)

elif task == "Webcam Live Feed":
    st.header("Webcam Live Object Detection")

    # Setup temporary file for video storage
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".avi")

    # OpenCV Video Capture
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Unable to access webcam.")
    else:
        st.text("Press 'Stop' button in Streamlit to quit.")

        # Process video frames
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Run YOLO inference
            results = model.predict(source=frame)

            # Annotate frame
            annotated_frame = results[0].plot()

            # Write annotated frame to temporary file
            cv2.imwrite(tmp_file.name, annotated_frame)

            # Display frame in Streamlit
            st.image(annotated_frame, channels="BGR", use_column_width=True)

            if st.button("Stop"):
                break

        cap.release()

    # Cleanup temporary file
    tmp_file.close()
