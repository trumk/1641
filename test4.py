import pandas as pd

# Đường dẫn đến tệp CSV gốc
csv_file_path = r'C:\Users\loan\OneDrive\Desktop\steam.csv'

# Đọc tệp CSV vào một DataFrame
df = pd.read_csv(csv_file_path)

# Lọc dữ liệu theo các điều kiện
filtered_df = df[
    (df["achievements"] != 0) &
    (df["positive_ratings"] != 0) &
    (df["negative_ratings"] != 0) &
    (df["average_playtime"] != 0) &
    (df["median_playtime"] != 0) &
    (df["price"] != 0)
]

# Chọn ra 700 dòng dữ liệu
filtered_df = filtered_df.head(700)

# Lưu kết quả vào một tệp CSV mới
filtered_csv_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'
filtered_df.to_csv(filtered_csv_path, index=False)
