import pandas as pd
import numpy as np

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'

df = pd.read_csv(csv_file_path, encoding='latin-1')

df['price'] = np.random.randint(500, 1201, size=len(df))

df.to_csv(csv_file_path, index=False)
