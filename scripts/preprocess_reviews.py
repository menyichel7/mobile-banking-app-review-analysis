import pandas as pd
import os

# Determine base path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Load raw reviews
raw_path = os.path.join(DATA_DIR, 'raw_reviews.csv')
df = pd.read_csv(raw_path)

# Drop duplicates and rows with missing values
df.drop_duplicates(inplace=True)
df.dropna(subset=['review', 'rating', 'date'], inplace=True)

# Convert date to standard format
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Add source and ensure 'bank' column exists
df['source'] = 'Google Play'
if 'bank' not in df.columns:
    df['bank'] = 'UNKNOWN'

# Save cleaned data
cleaned_path = os.path.join(DATA_DIR, 'cleaned_reviews.csv')
df.to_csv(cleaned_path, index=False)

print("Preprocessing complete. Cleaned data saved to data/cleaned_reviews.csv")
