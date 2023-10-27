import pandas as pd
import numpy as np

csv_file_path = r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv'

df = pd.read_csv(csv_file_path, encoding='latin-1')

countries_in_southeast_asia = ["Vietnam", "Thailand", "Indonesia", "Malaysia", "Singapore", "Philippines", "Myanmar", "Cambodia", "Laos", "Brunei", "Timor-Leste"]

def generate_region():
    region = np.random.choice(countries_in_southeast_asia, max(5, np.random.randint(1, 4)), replace=False)
    return ", ".join(region)

df['region'] = df.apply(lambda row: generate_region(), axis=1)

df.to_csv(r'C:\Users\loan\OneDrive\Desktop\filtereddata.csv', index=False)
