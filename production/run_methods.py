from ultralytics import YOLO
import cv2
import os

def run_yolo(model_loc, inference_input_path, inference_output_path):


    # Load the YOLO model
    model = YOLO(model_loc)

    # Run the inference
    results = model.predict(
        source=inference_input_path,
        conf=0.5,  # Confidence threshold
        iou=0.45,  # IoU threshold
        save=True,           # Save the results to disk
        save_txt=False,       # Save the results in label files
        project=inference_output_path, # Specify the project directory
        name=".",       # Subfolder name for results
        exist_ok=True,       # Allow overwriting
        show=True            # Display results in a popup (useful for debugging)
    )
    return results



def run_webcam_smoothly(model_path):
    """
    Run YOLO inference smoothly on the webcam with an option to stop.
    
    Args:
        model_path (str): Path to the YOLO model file.
    """
    # Load YOLO model
    model = YOLO(model_path)

    print("Press 'q' in the webcam window to quit.")

    try:
        # Run YOLO inference directly on the webcam (index 0)
        results = model.predict(
                            source=0,
                            conf=0.5,  # Confidence threshold
                            iou=0.45,  # IoU threshold
                            show=True, 
                            stream=True
                            )
        
        for result in results:
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Quitting...")
                break
    except KeyboardInterrupt:
        print("Interrupted! Exiting...")

    finally:
        # Clean up resources and close any OpenCV windows
        cv2.destroyAllWindows()
        print("Resources released. Goodbye!")