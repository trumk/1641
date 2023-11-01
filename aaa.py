import pandas as pd
import csv

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'

# Đọc dữ liệu từ tệp CSV và xử lý các giá trị không hợp lệ
valid_lines = []
with open(csv_file_path, 'r', encoding='latin-1') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Đọc header
    valid_lines.append(header)
    for line in csv_reader:
        if len(line) == len(header):  # Chỉ xử lý các dòng có đúng số lượng cột
            valid_lines.append(line)

# Tạo DataFrame từ danh sách các dòng hợp lệ
df = pd.DataFrame(valid_lines[1:], columns=valid_lines[0])

# Chuyển cột "release_date" sang kiểu dữ liệu datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Lọc bỏ các dòng với giá trị "release_date" không hợp lệ
df = df.dropna(subset=['release_date'])

# Trích xuất năm từ cột "release_date"
df['release_year'] = df['release_date'].dt.year

# Xác định năm tối đa và tối thiểu từ dữ liệu
min_year = df['release_year'].min()
max_year = df['release_year'].max()

# Tạo các cột mới dựa trên các năm
for year in range(min_year, max_year + 1):
    # Lọc các dòng thỏa mãn năm và tính tổng positive ratings cho năm đó
    df[f'positive_ratings_{year}'] = df[df['release_year'] == year]['positive_ratings'].sum()

# Lưu kết quả vào tệp CSV
df.to_csv(csv_file_path, index=False)
