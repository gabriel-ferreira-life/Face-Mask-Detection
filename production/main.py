import cv2
import os
import json
from ultralytics import YOLO
from run_methods import *

def main():
    # Load the config file
    with open('config.json', 'r') as f:
        config = json.load(f)

    file_id = config['file_id']
    url = config['url'].replace("file_id", file_id)
    model_output_path = config['model_output_path']
    model_output_file = config['model_output_file']
    model_loc = os.path.join(model_output_path, model_output_file)
    base_inference_files_path = config['base_inference_files_path']
    image_input_path = os.path.join(base_inference_files_path, "images/input")
    image_output_path = os.path.join(base_inference_files_path, "images/output")
    video_input_path = os.path.join(base_inference_files_path, "videos/input")
    video_output_path = os.path.join(base_inference_files_path, "videos/output")

   # Get user input
    print("Please choose the desired method:")
    print("  - 1 for image processing")
    print("  - 2 for live webcam processing")
    print("  - 3 for video processing")
    try:
        method = int(input("Enter your choice (1, 2, or 3): "))
    except ValueError:
        print("Error: Invalid input. Please enter a number (1, 2, or 3).")
        return

    # Execute the selected method
    if method == 1:
        # Validate image file extension
        valid_image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
        run_yolo(model_loc, image_input_path, image_output_path)
    elif method == 2:
        run_webcam_smoothly(model_loc)
    elif method == 3:
        run_yolo(model_loc, video_input_path, video_output_path)
    else:
        print("Error: Invalid method selected. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()