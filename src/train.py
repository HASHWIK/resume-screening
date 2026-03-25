import sys
import os

# FIX PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from config import DATA_PATH, MODEL_PATH

# Load data
df = pd.read_csv(DATA_PATH)

# Train vectorizer
vectorizer = TfidfVectorizer()
vectorizer.fit(df["resume"])

# Save model
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(vectorizer, MODEL_PATH)

print("Vectorizer saved successfully ✅")