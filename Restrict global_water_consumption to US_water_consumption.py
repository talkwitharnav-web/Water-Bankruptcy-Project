import pandas as pd
from pathlib import Path
# Finding working directory!
# .parent arguement makes it so it finds the folder in which this py file is in (our working directory) instead of just this file.
BASE_DIR = Path(__file__).parent
# Defining where the dataset is
DATA_FILE = BASE_DIR / "global_water_consumption_2000_2025.csv"
# Defining where the new dataset should be saved
OUTPUT_FILE = BASE_DIR / "US_water_consumption_2000_2025.csv"
# Reading the dataset
df = pd.read_csv(DATA_FILE)
# Filtering the dataset to only include rows where the country is the United States
us_df = df[df["Country"] == "USA"]
# Saving the new dataset to a new CSV file
us_df.to_csv(OUTPUT_FILE, index=False)
# Saving cleaned dataset to Clean Datasets folder
output_path = BASE_DIR / "Clean Datasets" / "US_water_consumption_2000_2025.csv"
us_df.to_csv(output_path, index=False)
print(f"Cleaned file saved to: {output_path}")
print(us_df.head())