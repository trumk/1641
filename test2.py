import pandas as pd
import numpy as np

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'

df = pd.read_csv(csv_file_path, encoding='latin-1')

#them cot region
# countries_in_southeast_asia = ["Vietnam", "Thailand", "Indonesia", "Malaysia", "Singapore", "Philippines", "Myanmar", "Cambodia", "Laos", "Brunei", "Timor-Leste"]

# df['region'] = [" ".join(np.random.choice(countries_in_southeast_asia, np.random.randint(1, 4))) for _ in range(len(df))]

df = df.drop('region', axis=1) #xoa cot region

df.to_csv(r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv', index=False)
