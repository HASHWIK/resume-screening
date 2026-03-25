import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# FIX PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import screen_candidates

st.set_page_config(page_title="Resume Screening Dashboard", layout="wide")

# =====================================================
# 🎨 PREMIUM STYLE
# =====================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Hover Button */
div.stButton > button {
    background-color: #1f2937;
    color: white;
    border-radius: 10px;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #3b82f6;
    transform: scale(1.05);
    box-shadow: 0px 0px 10px rgba(59,130,246,0.7);
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================
st.title("📄 AI Resume Screening Dashboard")
st.markdown("Smart candidate ranking & skill gap analysis")

# =====================================================
# BUTTON
# =====================================================
if st.button("🚀 Analyze Candidates"):

    df, job_desc, job_skills = screen_candidates()

    # =====================================================
    # 📌 JOB INFO
    # =====================================================
    st.markdown("## 📌 Job Description")
    st.info(job_desc)

    st.markdown("### 🧠 Required Skills")
    st.write(job_skills)

    # =====================================================
    # 📊 KPI CARDS
    # =====================================================
    st.markdown("## 🚀 Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Candidates", len(df))
    col2.metric("Top Score", f"{df['Score'].max()}%")
    col3.metric("Avg Score", f"{df['Score'].mean():.2f}%")

    # =====================================================
    # 🏆 TOP CANDIDATE
    # =====================================================
    top = df.iloc[0]

    st.markdown("## 🥇 Best Candidate")
    st.success(f"{top['name']} → Score: {top['Score']}%")

    # =====================================================
    # 📋 TABLE
    # =====================================================
    st.markdown("## 📋 Candidate Ranking")
    st.dataframe(df, use_container_width=True)

    # =====================================================
    # 📊 ANALYTICS
    # =====================================================
    st.markdown("## 📊 Analytics")

    col1, col2 = st.columns(2)

    # Bar Chart
    with col1:
        st.subheader("Score Distribution")
        st.bar_chart(df.set_index("name")["Score"])

    # Donut Chart
    with col2:
        st.subheader("Top Candidates Share")
        fig, ax = plt.subplots()
        top_scores = df.head(3)
        ax.pie(top_scores["Score"], labels=top_scores["name"], autopct='%1.1f%%')
        centre = plt.Circle((0,0),0.70,fc='black')
        fig.gca().add_artist(centre)
        st.pyplot(fig)

    # =====================================================
    # 📈 TIMELINE ANALYTICS 🔥
    # =====================================================
    st.markdown("## 📈 Candidate Score Timeline")

    timeline_df = df.copy()
    timeline_df["Time"] = pd.date_range(end=pd.Timestamp.now(), periods=len(df))
    timeline_df = timeline_df.sort_values("Time")

    st.line_chart(
        timeline_df.set_index("Time")["Score"]
    )

    # =====================================================
    # ⚠️ SKILL GAP
    # =====================================================
    st.markdown("## ⚠️ Skill Gap Analysis")

    for _, row in df.iterrows():
        st.write(f"**{row['name']}** → Missing: {row['Missing Skills']}")

    # =====================================================
    # DOWNLOAD
    # =====================================================
    st.download_button(
        "📥 Download Ranking",
        df.to_csv(index=False),
        "ranking.csv"
    )

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.markdown("💎 Premium Resume AI System | Task 3 Completed 🚀")