import pandas as pd
import numpy as np

df = pd.read_csv("data/HR_Job_Placement_Dataset.csv")

print("Shape:", df.shape)
print(df.info())
print(df.head())

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

for col in cat_cols:
    df[col] = df[col].str.lower().str.strip()

df['status'] = df['status'].map({'placed': 1, 'not placed': 0})

df.to_csv("data/cleaned_data.csv", index=False)

print("Cleaning completed")