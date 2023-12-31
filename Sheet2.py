import pandas as pd

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'

df = pd.read_csv(csv_file_path, encoding='latin-1')

df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year

games_2015 = df[df['release_year'] == 2015]

top_8_achievements = games_2015.sort_values(by='achievements', ascending=False).head(8)

print(top_8_achievements)
