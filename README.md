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
2. Run the following main.py in the `production` directory:

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

>> └── **test** # Testing data (images and labels)

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


