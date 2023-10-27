import pandas as pd
import numpy as np

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv(r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv')

# Đảm bảo cột "release_date" là kiểu dữ liệu datetime (nếu chưa)
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Lọc ra các trò chơi phát hành vào năm 2013
games_in_2013 = df[df['release_date'].dt.year == 2013]

# Sắp xếp theo ngày phát hành
games_in_2013 = games_in_2013.sort_values(by='release_date')

# Chọn 15 trò chơi đầu tiên
random_games_2013 = games_in_2013.head(15)

# In danh sách 15 trò chơi ngẫu nhiên của năm 2013
print(random_games_2013)
