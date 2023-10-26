import pandas as pd

# Đường dẫn đến tệp CSV
csv_file_path = r'C:\Users\loan\OneDrive\Desktop\steam.csv'

# Đọc tệp CSV vào một DataFrame
df = pd.read_csv(csv_file_path)

# Nhóm theo nhà phát triển và tính tổng số lượng đánh giá tiêu cực
developer_negative_ratings = df.groupby('developer')['negative_ratings'].sum().reset_index()

# Sắp xếp theo tổng số lượng đánh giá tiêu cực giảm dần
developer_negative_ratings = developer_negative_ratings.sort_values(by='negative_ratings', ascending=False)

# Chọn 8 nhà phát triển có số lượng đánh giá tiêu cực nhiều nhất
top_8_developers = developer_negative_ratings.head(8)

# In ra danh sách 8 nhà phát triển này
print(top_8_developers)
