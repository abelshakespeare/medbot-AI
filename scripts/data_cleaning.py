import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/abelshakespeare/Documents/GitHub/medbot-AI/data/raw/peerj-cs-08-1147-s001.csv')

# Filling missing 'Nationality' values with a placeholder if you expect all rows to have some value
df['Nationality'] = df['Nationality'].fillna('Unknown')

# Alternatively, if you need to drop rows where 'Nationality' is critical and should not be missing
# df = df.dropna(subset=['Nationality'])

# Remove duplicates (considering all columns)
df_no_duplicates = df.drop_duplicates()

# Save the cleaned data to a new CSV file
df_no_duplicates.to_csv('/Users/abelshakespeare/Documents/GitHub/medbot-AI/data/raw/peerj-cs-08-1147-s001.csv', index=False)