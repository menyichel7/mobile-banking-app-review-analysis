import pandas as pd

# Load raw reviews
df = pd.read_csv('../data/raw_reviews.csv')

# Drop duplicates and rows with missing values
df.drop_duplicates(inplace=True)
df.dropna(subset=['review', 'rating', 'date'], inplace=True)

# Convert date to standard format
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Add source and ensure 'bank' column exists
df['source'] = 'Google Play'
if 'bank' not in df.columns:
    df['bank'] = 'UNKNOWN'  # Placeholder if not present

# Save cleaned data
df.to_csv('../data/cleaned_reviews.csv', index=False)

print("Preprocessing complete. Cleaned data saved to data/cleaned_reviews.csv")
