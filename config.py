import os

# Get base project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------
# DATA FILES
# -----------------------------
DATA_PATH = os.path.join(BASE_DIR, "data", "resumes.csv")
JOB_DESC_PATH = os.path.join(BASE_DIR, "data", "job_description.txt")

# -----------------------------
# MODEL FILE
# -----------------------------
MODEL_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# -----------------------------
# OPTIONAL (for future use)
# -----------------------------
REPORT_PATH = os.path.join(BASE_DIR, "reports", "report.txt")