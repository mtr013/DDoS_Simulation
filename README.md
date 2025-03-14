# Real-Time Detection of DDoS Attacks Using Machine Learning in a Simulated Network Environment

## Overview

This project aims to develop a real-time system for detecting **Distributed Denial of Service (DDoS) attacks** using **machine learning** techniques. The focus is on identifying and mitigating different types of DDoS attacks in a simulated network environment using machine learning models such as **Random Forest**, **Support Vector Machine (SVM)**, and **XGBoost**. The system is trained using datasets such as **CIC-DDoS 2019** and **CAIDA DDoS 2007**, both of which provide network traffic data under normal conditions and during DDoS attacks.

## Features
- Real-time simulation of DDoS attacks.
- Machine learning models trained on **CIC-DDoS 2019** and **CAIDA DDoS 2007** datasets.
- Use of feature engineering to extract relevant features for training.
- Evaluation of models using performance metrics like accuracy, precision, recall, and F1 score.
- Modular code structure to easily extend with additional models or datasets.

## Datasets

### CIC-DDoS 2019 Dataset
The **CIC-DDoS 2019** dataset contains network traffic data for various types of DDoS attacks and normal traffic. This dataset has been preprocessed to include features such as packet size, protocol type, and flow duration. It is available in **CSV format**.

### CAIDA DDoS 2007 Dataset
The **CAIDA DDoS 2007** dataset contains **PCAP** files with DDoS traffic and background traffic. This dataset is used to evaluate the model's ability to detect attacks at the packet level. 

## Installation

To run the project and replicate the results, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/real-time-ddos-detection.git
