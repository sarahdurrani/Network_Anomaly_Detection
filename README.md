# Network Anomaly Detection
This project is a part of the AAI-540 course in the Applied Artificial Intelligence Program at the University of San Diego (USD).

## Project Status: Completed
This project aims to detect network anomalies and potential cyber threats using machine learning models trained on network traffic data.

## Project Structure
AAI-540 Project/
│── Datasets/                      <- Raw dataset (excluded from GitHub)
│── Processed Datasets/            <- Processed dataset (excluded from GitHub)
│── Data Processing.ipynb          <- Notebook for data preprocessing
│── EDA.ipynb                      <- Notebook for exploratory data analysis
│── Feature Engineering.ipynb      <- Notebook for feature engineering
│── Uploading files to S3.ipynb    <- Notebook for S3 uploads
│── requirements.txt                <- Lists dependencies
│── README.md                       <- Project documentation
│── .gitignore                      <- Prevents unnecessary files from being committed

## Project Overview
Network Anomaly Detection focuses on identifying abnormal behavior in network traffic that may indicate cyber threats such as DDoS attacks, port scans, web attacks, and infiltrations.
The dataset used consists of NetFlow logs and syslog data, and machine learning models will be applied to classify normal vs. anomalous traffic.

## Key Objectives
Preprocess raw network flow data into a structured format.
Perform EDA to analyze traffic patterns and attack distributions.
Extract meaningful features for machine learning classification.
Train & evaluate ML models to detect network anomalies.
Deploy the model for real-time monitoring.

## Installation and Setup
### Clone the Repository 
git clone https://github.com/sarahdurrani/Network_Anomaly_Detection.git
cd Network_Anomaly_Detection
### Install Dependencies
pip install -r requirements.txt
### Run Jupyter Notebooks 
Execute the following notebooks in order:
1. Data Processing.ipynb → Cleans and preprocesses network flow data.
2. EDA.ipynb → Performs Exploratory Data Analysis (EDA).
3. Feature Engineering.ipynb → Extracts and selects features for ML.
3. Uploading files to S3.ipynb → Uploads datasets to AWS S3.

## Dataset Details 
The dataset consists of multiple CSV files representing network activity across different days. It includes both normal traffic (BENIGN) and various network attacks:

DDoS (Distributed Denial of Service)
Port Scanning
Web Attacks (Brute Force, XSS)
Infiltrations
Other cyber threats
Processed datasets are stored in the Processed Datasets/ directory and uploaded to AWS S3.

## Methods Used
### Data Preprocessing
Removed missing values and inconsistencies.
Standardized and encoded categorical values.
Normalized numerical features for better model performance.
### Exploratory Data Analysis (EDA)
Class distribution of normal vs. attack traffic.
Feature correlations and outlier detection.
Visualization of network flow patterns.
### Feature Engineering
Selected relevant network features for anomaly detection.
Performed scaling & transformation to improve model performance.
Handled imbalanced data using sampling techniques.

## Technologies Used
Python 
Pandas (Data Processing)
Matplotlib / Seaborn (Data Visualization)
Scikit-learn (Feature Engineering & Machine Learning)
Boto3 (AWS S3 Integration)
Jupyter Notebooks (Development Environment)

## Future Work
Train and evaluate ML models: Implement Random Forest, XGBoost, LSTMs, and CNNs to classify network anomalies.
Hyperparameter tuning: Optimize model performance using GridSearchCV.
Deployment: Develop a real-time monitoring tool using Flask API or AWS Lambda.

## License
This project is open-source and available under the MIT License.

## Author: Sarah Durrani
🔗 GitHub Repository: Network Anomaly Detection
