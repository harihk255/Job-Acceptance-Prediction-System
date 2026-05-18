import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/final_data.csv")

st.title("Job Acceptance Prediction Dashboard")

total_candidates = len(df)
placement_rate = df['status'].mean() * 100
avg_interview = df['interview_performance'].mean()
avg_skills = df['skills_match_percentage'].mean()
dropout_rate = 100 - placement_rate
high_risk = len(df[df['status'] == 0]) / len(df) * 100

st.write("Total Candidates:", total_candidates)
st.write("Placement Rate (%):", round(placement_rate, 2))
st.write("Job Acceptance Rate (%):", round(placement_rate, 2))
st.write("Average Interview Score:", round(avg_interview, 2))
st.write("Average Skills Match %:", round(avg_skills, 2))
st.write("Offer Dropout Rate (%):", round(dropout_rate, 2))
st.write("High Risk Candidates (%):", round(high_risk, 2))

st.subheader("Interview Score vs Acceptance")
fig1 = plt.figure()
sns.boxplot(x='status', y='interview_performance', data=df)
st.pyplot(fig1)

st.subheader("Skills vs Placement")
fig2 = plt.figure()
sns.boxplot(x='status', y='skills_match_percentage', data=df)
st.pyplot(fig2)

st.subheader("Company Tier vs Acceptance")
fig3 = plt.figure()
sns.countplot(x='company_tier', hue='status', data=df)
st.pyplot(fig3)