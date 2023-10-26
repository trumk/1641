import pandas as pd

# Đường dẫn đến tệp CSV
csv_file_path = r'C:\Users\loan\OneDrive\Desktop\steam.csv'

# Đọc tệp CSV vào một DataFrame
df = pd.read_csv(csv_file_path)

# Sắp xếp DataFrame theo cột "average_playtime" theo thứ tự giảm dần
df = df.sort_values(by='average_playtime', ascending=False)

# Chọn 8 tựa game có average_playtime cao nhất
top_8_games = df.head(8)

# In ra danh sách 8 tựa game này
print(top_8_games)
