import pandas as pd

# Đường dẫn đến tệp CSV
csv_file_path = r'C:\Users\loan\OneDrive\Desktop\steam.csv'

# Đọc tệp CSV vào một DataFrame
df = pd.read_csv(csv_file_path)

# Loại bỏ dữ liệu không mong muốn trong cột "name" (ví dụ: loại bỏ ký tự "$")
df['name'] = df['name'].str.replace('$', '')

half_rows = len(df) // 2  # Chọn nửa dữ liệu
df = df.iloc[:half_rows]

df.to_csv(csv_file_path, index=False)

