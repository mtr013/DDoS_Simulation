# DDoS Attack Detection Pipeline

![DDoS Detection](https://img.shields.io/badge/Type-ML_Pipeline-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Dataset](https://img.shields.io/badge/Dataset-CIC--DDoS2019-red)
![Simulation](https://img.shields.io/badge/Network-Kathará-yellow)

## Overview

A machine learning pipeline for detecting SYN, UDP, and HTTP DDoS attacks using the [CIC-DDoS2019 Dataset](https://data.mendeley.com/datasets/ssnc74xm6r/1), tested with the [CAIDA DDoS Dataset](https://catalog.caida.org/dataset/ddos_attack_2007). The pipeline integrates Random Forest, SVM, and XGBoost models for attack detection.

## Setup

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt --ignore-installed
   ```
2. **Download Datasets:**

- Download the [CIC-DDoS2019 Dataset](https://data.mendeley.com/datasets/ssnc74xm6r/1) and place the files in a `data/` folder inside the project directory.

- Optionally, you can download the [CAIDA DDoS Dataset](https://catalog.caida.org/dataset/ddos_attack_2007) DDoS Dataset for additional testing and place it in the same `data/` folder.

3. **Docker & Kathara Setup:**

- Ensure Docker is installed and running.

- Install Kathara for network simulation.

## Running the Simulation

- Start the simulation environment with Docker:

```bash
docker-compose up
```
- Run the network simulation:

```bash
python -m kathara lstart
```

- Use `hping3`, `loic`, `slowris` to simulate traffic

#### **Note:** Only simulation testing and synthetic flow-level data were used. No packet capture tools like Wireshark or CAIDA PCAPs were analysed.

- Run the detection pipeline:

Launch Jupyter Notebook:

```bash
jupyter notebook
```

- Open `ddos_detection.ipynb` to detect DDoS attacks using the trained models.

## Demo Guide

To reproduce the demo shown:

1. Train or load pre-trained models (in `models/` folder).
2. Launch the pipeline notebook: `ddos_detection.ipynb`
3. Start simulation with Docker and Kathará.
4. Inject attacks using tools like `hping3`, `loic`, and `slowloris`.
5. Observe real-time logs, alerts, and detector performance.

## Models

The following trained models are used:

- `tuned_randomforest_model.pkl`
- `tuned_sgd_model.pkl`
- `tuned_xgboost_model.pkl`

These are loaded automatically by the real-time detection script. You can retrain or replace them by running the full pipeline.

## Requirements

- Python 3.11 (tested)
- RAM: ≥ 8 GB recommended
- Docker + Kathará

## Folder Structure

```bash
DDoS_Simulation/
├── data/
│   └── cicddos2019_dataset.csv                  # Raw dataset for training/testing
│
├── docker/
│   └── Dockerfile                               # Docker image setup
│
├── kathara/
│   └── lab.conf                                 # Kathará network configuration
│
├── models/
│   ├── label_encoder.pkl                        # Label encoder for classes
│   ├── preprocessor.pkl                         # Feature scaler/preprocessing
│   ├── random_forest_model.pkl                  # Trained RF model
│   ├── svm_sgd_model.pkl                        # Trained SGD SVM model
│   ├── xgboost_model.pkl                        # Trained XGBoost model
│   ├── tuned_randomforest_model.pkl             # Tuned RF model
│   ├── tuned_sgd_model.pkl                      # Tuned SVM model
│   └── tuned_xgboost_model.pkl                  # Tuned XGBoost model
│
├── results/
│   ├── error_analysis/
│   │   ├── error_details.csv
│   │   ├── RandomForestClassifier_error_confidence.png
│   │   └── RandomForestClassifier_error_types.png
│   │
│   ├── metrics/
│   │   ├── attack_performance.csv
│   │   ├── cv_score_table.csv
│   │   ├── final_cv_scores.json
│   │   ├── final_metrics.json
│   │   ├── final_tuned_metrics.json
│   │   ├── final_tuned_summary.csv
│   │   ├── model_comparison.csv
│   │   ├── RandomForest_tuning_results.csv
│   │   ├── SGD_tuning_results.csv
│   │   ├── tuning_summary.csv
│   │   └── XGBoost_tuning_results.csv
│   │
│   └── plots/
│       ├── confusion_matrices/
│       │   ├── RandomForest_confusion.png
│       │   ├── SVM_confusion.png
│       │   └── XGBoost_confusion.png
│       │
│       ├── feature_analysis/
│       │   ├── correlation_heatmap.png
│       │   ├── num__Flow_Duration_distribution.png
│       │   └── num__Fwd_Packets_s_distribution.png
│       │
│       ├── feature_importance/
│       │   ├── RandomForest.png
│       │   └── XGBoost.png
│       │
│       ├── performance_curves/
│       │   └── XGBoost_training.png
│       │
│       ├── tuning/
│       │   ├── RandomForest_tuning_curve.png
│       │   ├── SGD_tuning_curve.png
│       │   └── XGBoost_tuning_curve.png
│       │
│       ├── svm_coefficients.png
│       ├── class_distribution.png
│       └── cv_score_summary.png
│
├── ddos_simulation.ipynb                       # Full pipeline: training, tuning, real-time
├── ddos_simulation.log                         # Log file from simulation run
├── docker-compose.yml                          # Compose file for multi-container setup
├── requirements.txt                            # Python dependencies
└── README.md                                   # Project overview

```