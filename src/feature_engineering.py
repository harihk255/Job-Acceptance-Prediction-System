import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

df['experience_category'] = pd.cut(
    df['years_of_experience'],
    bins=[-1, 1, 5, 50],
    labels=['fresher', 'junior', 'senior']
)

df['skills_level'] = pd.cut(
    df['skills_match_percentage'],
    bins=[0, 40, 70, 100],
    labels=['low', 'medium', 'high']
)

df['interview_performance'] = (
    df['technical_score'] +
    df['aptitude_score'] +
    df['communication_score']
) / 3

df['interview_category'] = pd.cut(
    df['interview_performance'],
    bins=[0, 40, 70, 100],
    labels=['poor', 'average', 'good']
)

df['academic_score'] = (
    df['ssc_percentage'] +
    df['hsc_percentage'] +
    df['degree_percentage']
) / 3

df['academic_category'] = pd.cut(
    df['academic_score'],
    bins=[0, 50, 75, 100],
    labels=['low', 'medium', 'high']
)

df['placement_score'] = (
    df['skills_match_percentage'] * 0.4 +
    df['interview_performance'] * 0.4 +
    df['academic_score'] * 0.2
)

df.to_csv("data/final_data.csv", index=False)

print("Feature engineering completed")