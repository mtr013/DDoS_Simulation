# DDoS Detection Using Machine Learning

## Overview

This project aims to detect Distributed Denial of Service (DDoS) attacks using machine learning techniques. The primary goal is to develop a model capable of identifying and classifying DDoS attack traffic from normal traffic in a network environment. This project involves data collection, preprocessing, feature extraction, model training, and evaluation using publicly available DDoS attack datasets. Machine learning algorithms like **Random Forest**, **SVM**, and **XGBoost** are used for attack detection.

## Objectives

1. **Preprocess and clean datasets** to extract relevant features for machine learning models.
2. **Train and evaluate machine learning models** using supervised learning techniques.
3. **Test the models on real-world DDoS attack data** to measure performance.
4. **Implement real-time DDoS detection** using the trained models.

The project will focus on two primary datasets:
- **CIC-DDoS 2019**
- **CAIDA DDoS 2007**

## Datasets

### 1. CIC-DDoS 2019
The **CIC-DDoS 2019** dataset contains various network traffic features collected from real-world DDoS attacks and normal traffic. This dataset provides information about network flow and traffic characteristics, including packet size, flow duration, protocol, and more. It is in **CSV format** and can be processed using Python libraries like **pandas**.

You can download the dataset from the [CIC-DDoS 2019 Dataset](https://www.unb.ca/cic/datasets/ddos-2019.html).

### 2. CAIDA DDoS 2007
The **CAIDA DDoS Attack 2007** dataset contains **PCAP files** that capture network traffic during a simulated DDoS attack. These packet captures provide detailed low-level network data that can be analyzed using tools like **Wireshark** or **Scapy**.

You can download the dataset from the [CAIDA DDoS 2007 Dataset](https://www.caida.org/catalog/datasets/ddos-20070804_dataset).

### How to Use the Datasets

1. **Download the datasets** from the provided links.
2. **Extract the datasets** into the `data` directory.
3. **CIC-DDoS 2019** data will be in CSV format, while **CAIDA DDoS 2007** will be in PCAP format.

---

## Methodology

The approach to DDoS attack detection is divided into the following steps:

### 1. **Data Preprocessing**
   - **CIC-DDoS 2019**: Clean the CSV data to handle missing values and outliers. Normalize the data to ensure uniformity across features.
   - **CAIDA DDoS 2007**: Convert the raw PCAP data into a usable format using **Scapy** or **Wireshark** to extract features relevant for classification.

### 2. **Feature Engineering**
   - Extract relevant features from the datasets, such as:
     - Packet size
     - Flow duration
     - Protocol type
     - Source/Destination IPs
     - Payload sizes
     - Number of packets per flow

### 3. **Model Training**
   - Use machine learning algorithms:
     - **Random Forest**
     - **Support Vector Machine (SVM)**
     - **XGBoost**
   - Split the dataset into training and testing sets (typically 80% for training, 20% for testing).
   - Train the models using the extracted features and evaluate their performance using accuracy, precision, recall, and F1 score.

### 4. **Evaluation and Testing**
   - Evaluate the models on test datasets to see how well they generalize to unseen data.
   - Use various performance metrics to evaluate the model’s accuracy in detecting DDoS attacks.

---

## Requirements

To run this project, you need to install the following Python packages:

- **pandas**: For data manipulation and preprocessing.
- **numpy**: For numerical operations.
- **scikit-learn**: For implementing machine learning models.
- **xgboost**: For advanced machine learning models.
- **scapy**: For working with PCAP files.
- **matplotlib** / **seaborn**: For visualizations.
  
You can install the required dependencies using `pip`:

```bash
pip install pandas numpy scikit-learn xgboost scapy matplotlib seaborn
