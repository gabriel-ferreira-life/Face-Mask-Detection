# Face Mask Detection Using YOLO v11n

This project focuses on developing a computer vision system for detecting face masks in images and videos using the YOLO (You Only Look Once) object detection framework. The system can classify faces into three categories: "With Mask," "Without Mask," and "Mask Worn Incorrectly." It supports real-time detection and has applications in public safety and healthcare.

---

## **Features**
- Real-time face mask detection on images, videos, and webcam feeds.
- Multi-face detection and classification into three mask-related categories.
- Accuracy with mAP@0.5 of **72.7%** using YOLO v11n.
- Configurable for different datasets and deployment environments.

---

## **Usage**
1. Install packages in the `requirements.txt`
2. Open Terminal and run the main.py in the `production` directory
3. Follow the instructions to choose the type of input (image, video, or live webcam video).

## **Directory Structure**
Face-Mask-Detection
> └── **production** 
>> ├── config.json # Configuration file with paths and hyperparameters \
>> ├── run_methods.py # Helper functions for inference \
>> ├── main.py # Main script for running the project 

> └── **model** # Pretrained and fine-tuned YOLO models
>> ├── yolo11n.pt 

> └── **data** # Directory for datasets 
>> └── **train** # Training data (images and labels)

>> └── **val** # Validation data (images and labels)

>> └── **test** # Testing data (images and labels) \
Obs.: train, val, test are not available in the remote repository due to its size. You will need to download it from Kaggle and use the `dataset_configuration.ipynb` to orginize this hierarchy.

>> └── **runs** # Results of each training experiment

>> └── **Inference** # Testing data (images and labels)
>>> └── **images** 
>>>> └── **input** \
>>>> └── **output** 

>>> └── **videos** 
>>>> └── **input** \
>>>> └── **output** 

> └── **model_training** 
>> ├── data_exploration.ipynb \
>> ├── dataset_configuration.ipynb \
>> ├── model_training.ipynb 

> └── **report** # Project documentation
>> ├── Face_Mask_Detection_With_YOLO11n.pdf

> ├── README.md \
> ├── requirements.txt

---

## **Acknowledgments**

This project would not have been possible without the resources and support provided by the following:

- **Dataset**:  
  The [Face Mask Detection Dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection) on Kaggle, which provided the labeled data necessary for training and evaluating the model.

- **Framework**:  
  The [Ultralytics YOLO](https://github.com/ultralytics/yolov5) framework, which served as the foundation for model training and inference.

- **Environment**:  
  Google Colab, for providing GPU resources that significantly accelerated the training process.

Special thanks to Professor Huai Mengdi and Aobo Chen for their guidance throughout this project, and to my peers for their valuable feedback and discussions.
