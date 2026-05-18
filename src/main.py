from preprocessing import load_data, preprocess_data
from eda import run_eda
from feature_engineering import create_features
from model.model import train_model

# Load data
df = load_data()

# Preprocess
df = preprocess_data(df)

# Feature Engineering
df = create_features(df)

# EDA
run_eda(df)

# Model
train_model(df)