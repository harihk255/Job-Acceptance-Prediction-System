# Job Acceptance Prediction System

## Project Overview

This project analyzes candidate data and predicts whether a candidate will accept or reject a job offer using machine learning.

## Problem Statement

Recruitment teams handle large volumes of candidate data, but not all candidates accept job offers.
This project builds a system to predict job acceptance and identify key factors influencing decisions.

## Dataset

* 51,500 candidate records
* Includes academic scores, skills, experience, interview performance, and job-related factors

## Project Steps

### 1. Data Cleaning

* Handled missing values using median and mode
* Fixed inconsistent categorical values

### 2. Exploratory Data Analysis (EDA)

* Interview score vs job acceptance
* Skills match vs placement
* Company tier vs acceptance
* Experience vs placement

### 3. Feature Engineering

* Experience category (Fresher, Junior, Senior)
* Skills level (Low, Medium, High)
* Interview performance category
* Academic performance category
* Placement score

### 4. Machine Learning Model

* Model used: Logistic Regression
* Target variable:

  * Placed = 1
  * Not Placed = 0
* Evaluated using accuracy, precision, recall, F1-score

### 5. Dashboard

* Built using Streamlit
* Displays key KPIs and visualizations

## Key KPIs

* Total Candidates
* Placement Rate (%)
* Job Acceptance Rate (%)
* Average Interview Score
* Average Skills Match %
* Offer Dropout Rate (%)
* High Risk Candidates (%)

## Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit


## How to Run

### Install dependencies

pip install -r requirements.txt

### Run preprocessing

python src/preprocessing.py

### Run feature engineering

python src/feature_engineering.py

### Train model

python src/model.py

### Run dashboard

streamlit run app/app.py

## Conclusion

The model helps predict job acceptance and provides insights to improve recruitment strategies.
