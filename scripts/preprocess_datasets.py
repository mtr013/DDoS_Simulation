import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_dataset.csv')  # Change this to your actual dataset path

# Data preprocessing
df = df.dropna()  # Remove rows with missing values
df = df[['feature1', 'feature2', 'label']]  # Select relevant columns
