import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned_data.csv")

print(df.head())

plt.figure()
sns.boxplot(x='status', y='technical_score', data=df)
plt.title("Interview Score vs Job Acceptance")
plt.show()

plt.figure()
sns.boxplot(x='status', y='skills_match_percentage', data=df)
plt.title("Skills Match vs Placement")
plt.show()

plt.figure()
sns.countplot(x='company_tier', hue='status', data=df)
plt.title("Company Tier vs Acceptance")
plt.show()

plt.figure()
sns.boxplot(x='status', y='years_of_experience', data=df)
plt.title("Experience vs Placement")
plt.show()

plt.figure()
sns.countplot(x='competition_level', hue='status', data=df)
plt.title("Competition Level vs Acceptance")
plt.show()

plt.figure()
corr = df.select_dtypes(include=['int64', 'float64']).corr()
sns.heatmap(corr, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()