# 📄 AI Resume Screening & Candidate Ranking System

An end-to-end Machine Learning system that automatically analyzes resumes, matches them with job descriptions, ranks candidates, and identifies skill gaps — all through an interactive dashboard.

---

## 🌐 Live Demo
👉 https://your-resume-app.streamlit.app

---

## 🎯 Project Overview

Recruiters often receive hundreds of resumes for a single role. This system automates the screening process using Natural Language Processing (NLP) and Machine Learning.

It compares resumes with a job description and ranks candidates based on relevance and skill matching.

---

## 🚀 Key Features

- 📄 Resume text preprocessing & cleaning  
- 🧠 Skill extraction from resumes  
- 🎯 Job description matching  
- 📊 Candidate ranking using similarity scores  
- ⚠️ Skill gap detection (missing skills)  
- 🏆 Best candidate identification  
- 📈 Interactive dashboard with analytics  
- 📥 Export results as CSV  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- NLP (Text Processing)  
- TF-IDF Vectorization  
- Streamlit (Dashboard)  
- Pandas & NumPy  

---

## 🧠 How It Works

1. Clean and preprocess resume text  
2. Convert text into numerical vectors using TF-IDF  
3. Compare resumes with job description using cosine similarity  
4. Assign scores to each candidate  
5. Rank candidates based on relevance  
6. Identify missing skills for each candidate  

---

## 📂 Project Structure
# 📄 AI Resume Screening & Candidate Ranking System

An end-to-end Machine Learning system that automatically analyzes resumes, matches them with job descriptions, ranks candidates, and identifies skill gaps — all through an interactive dashboard.

---

## 🌐 Live Demo
👉 https://your-resume-app.streamlit.app

---

## 🎯 Project Overview

Recruiters often receive hundreds of resumes for a single role. This system automates the screening process using Natural Language Processing (NLP) and Machine Learning.

It compares resumes with a job description and ranks candidates based on relevance and skill matching.

---

## 🚀 Key Features

- 📄 Resume text preprocessing & cleaning  
- 🧠 Skill extraction from resumes  
- 🎯 Job description matching  
- 📊 Candidate ranking using similarity scores  
- ⚠️ Skill gap detection (missing skills)  
- 🏆 Best candidate identification  
- 📈 Interactive dashboard with analytics  
- 📥 Export results as CSV  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- NLP (Text Processing)  
- TF-IDF Vectorization  
- Streamlit (Dashboard)  
- Pandas & NumPy  

---

## 🧠 How It Works

1. Clean and preprocess resume text  
2. Convert text into numerical vectors using TF-IDF  
3. Compare resumes with job description using cosine similarity  
4. Assign scores to each candidate  
5. Rank candidates based on relevance  
6. Identify missing skills for each candidate  

---

## 📂 Project Structure
resume_screening/
│
├── dashboard/ # Streamlit UI
├── src/ # ML logic (train, predict, preprocess)
├── data/ # Resume dataset & job description
├── models/ # Trained vectorizer
├── config.py
├── requirements.txt


---

## ⚙️ Installation & Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/resume-screening.git

# Navigate to folder
cd resume-screening

# Install dependencies
pip install -r requirements.txt

# Train model
python src/train.py

# Run application
streamlit run dashboard/app.py
