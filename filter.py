import pandas as pd

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\steam.csv'

df = pd.read_csv(csv_file_path)

filtered_df = df[
    (df["achievements"] != 0) &
    (df["positive_ratings"] != 0) &
    (df["negative_ratings"] != 0) &
    (df["average_playtime"] != 0) &
    (df["median_playtime"] != 0) &
    (df["price"] != 0)
]

filtered_df = filtered_df.head(700)

filtered_csv_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'
filtered_df.to_csv(filtered_csv_path, index=False)
