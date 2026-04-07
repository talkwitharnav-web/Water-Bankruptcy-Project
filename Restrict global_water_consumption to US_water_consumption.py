import pandas as pd
from pathlib import Path
# Finding working directory!
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
# .unlink() (delete) the original dataset because it's now useless
DATA_FILE.unlink()