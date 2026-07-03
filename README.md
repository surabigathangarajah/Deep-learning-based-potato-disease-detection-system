# Deep-learning-based-potato-disease-detection-system
End-to-end deep learning project for potato leaf disease classification using CNN with deployment via FastAPI, TensorFlow Serving, and mobile/web applications.
Potato Disease Classification Using CNN

An end-to-end Deep Learning project that classifies potato leaf diseases using Convolutional Neural Networks (CNN). The system detects whether a potato plant is healthy or affected by Early Blight or Late Blight using leaf images.

Problem Statement

Potato crops are affected by diseases such as Early Blight and Late Blight, which reduce yield and cause economic loss.

This project builds an AI system that helps farmers detect diseases using a simple leaf image.

Features
CNN-based image classification model
Detects: Healthy, Early Blight, Late Blight
Data preprocessing and augmentation
FastAPI backend for inference
TensorFlow Serving for deployment
React.js web application
React Native mobile application
TensorFlow Lite optimization for mobile deployment
Deployment on Google Cloud Platform (GCP)
Architecture

Image → Preprocessing → CNN Model → API (FastAPI / TensorFlow Serving) → Frontend / Mobile App → GCP Deployment

Tech Stack

Deep Learning:

TensorFlow
Keras
CNN

Backend:

FastAPI
TensorFlow Serving

Frontend:

React.js
React Native

Deployment:

TensorFlow Lite
Google Cloud Platform (GCP)
Project Structure

Potato-Disease-Classification/

dataset/
training/
api/
frontend/
mobile-app/
tf-serving/
saved_models/
tflite-model/
notebooks/
requirements.txt
Model Workflow
Data collection
Data preprocessing
Data augmentation
CNN model building
Model training
Model evaluation
Model saving
Model deployment
Applications

Web Application:

Upload image
Get prediction

Mobile Application:

Capture image
Offline prediction using TensorFlow Lite
Deployment
FastAPI + TensorFlow Serving for backend
TensorFlow Lite for mobile optimization
Google Cloud Platform (GCP) hosting
Dataset

Classes:

Healthy
Early Blight
Late Blight

Preprocessing:

Resize images
Normalize pixel values
Data augmentation (flip, rotation, zoom)
Future Improvements
Add more crop disease datasets
Improve accuracy using transfer learning
Add explainability using Grad-CAM
Dockerize the project
CI/CD pipeline integration
