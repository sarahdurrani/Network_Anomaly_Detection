# Network_Anomaly_Detection

## Project Structure
AAI-540 Project/ │── Datasets/ <- Raw dataset (excluded from GitHub) │── Processed Datasets/ <- Processed dataset (excluded from GitHub) │── Data Processing.ipynb <- Notebook for data preprocessing │── EDA.ipynb <- Notebook for exploratory data analysis │── Feature Engineering.ipynb <- Notebook for feature engineering │── Uploading files to S3.ipynb <- Notebook for S3 uploads │── requirements.txt <- Lists dependencies │── README.md <- Project documentation │── .gitignore <- Prevents unnecessary files from being committed

## Setup Instructions 
---
```markdown
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/sarahdurrani/Network_Anomaly_Detection.git
cd Network_Anomaly_Detection

## Install Dependencies
pip install -r requirements.txt

---

#### Dataset Details**
---
```markdown
### 🔍 **Dataset Details**
The dataset consists of multiple CSV files representing different days of network activity, including:
- Normal traffic (`BENIGN`)
- Various network attacks (e.g., **DDoS, Port Scans, Web Attacks, Infiltrations**)

The processed dataset files are saved in the **Processed Datasets/** directory and uploaded to **AWS S3**.
---
## Future Work
---
- Implement **Machine Learning models** (Random Forest, XGBoost, etc.).
- Evaluate performance with **ROC-AUC, Precision, Recall, and F1-score**.
- Deploy the trained model using **AWS Lambda or Flask API**.
