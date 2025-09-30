import pandas as pd

# Load dataset
df = pd.read_csv('../dataset/sample.csv')

# Example preprocessing:
# - Lowercase all text
# - Strip whitespace from labels
df['text'] = df['text'].str.lower()
df['label'] = df['label'].str.strip()

# Save cleaned dataset
df.to_csv('../dataset/sample_clean.csv', index=False)

print("Preprocessing done. Saved as sample_clean.csv")
