import sys
import os

# FIX PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from config import DATA_PATH, MODEL_PATH, JOB_DESC_PATH
from src.preprocess import clean_text

# Load model
vectorizer = joblib.load(MODEL_PATH)

def extract_skills(text):
    skills = ["python", "machine learning", "nlp", "sql", "excel", "java", "spring"]
    text = text.lower()
    return [skill for skill in skills if skill in text]

def screen_candidates():
    df = pd.read_csv(DATA_PATH)

    with open(JOB_DESC_PATH, "r") as f:
        job_desc = f.read()

    job_clean = clean_text(job_desc)
    resumes_clean = df["resume"].apply(clean_text)

    job_vec = vectorizer.transform([job_clean])
    resume_vec = vectorizer.transform(resumes_clean)

    scores = cosine_similarity(job_vec, resume_vec)[0]

    df["Score"] = (scores * 100).round(2)

    # Extract skills
    df["Skills"] = df["resume"].apply(extract_skills)

    job_skills = extract_skills(job_desc)

    # Skill gap
    df["Missing Skills"] = df["Skills"].apply(
        lambda s: list(set(job_skills) - set(s))
    )

    # Sort
    df = df.sort_values(by="Score", ascending=False)

    return df, job_desc, job_skills