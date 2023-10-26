import pandas as pd

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'

df = pd.read_csv(csv_file_path, encoding='latin-1')

filtered_df = df[(df['price'] >= 10) & (df['price'] <= 20)]

filtered_df = filtered_df.sort_values(by='average_playtime', ascending=False)

top_5_games = filtered_df.head(5)

print(top_5_games)
