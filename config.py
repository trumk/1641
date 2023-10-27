import pandas as pd
import numpy as np

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'

df = pd.read_csv(csv_file_path, encoding='latin-1')

df['owners'] = np.random.randint(20000000, 200000000, len(df))

df.to_csv(r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv', index=False)



