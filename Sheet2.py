import pandas as pd

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'


df = pd.read_csv(csv_file_path, encoding='latin-1')


df = df.sort_values(by='achievements', ascending=False)


top_8_achievements = df.head(8)


print(top_8_achievements)
