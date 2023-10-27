import pandas as pd
import numpy as np
# Đọc dữ liệu từ tệp CSV
df = pd.read_csv(r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv')

df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

games_in_2013 = df[df['release_date'].dt.year == 2013]

games_in_2013 = games_in_2013.sort_values(by='release_date')

random_games_2013 = games_in_2013.head(15)

print(random_games_2013)
