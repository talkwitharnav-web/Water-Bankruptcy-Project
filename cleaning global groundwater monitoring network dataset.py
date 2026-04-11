import pandas as pd
from pathlib import Path
# Finding working directory!
# .parent arguement makes it so it finds the folder in which this py file is in (our working directory) instead of just this file.
BASE_DIR = Path(__file__).parent
""" # Defining where the dataset is
DATA_FILE = BASE_DIR / "Global Groundwater Monitoring Network dataset.csv"
# Defining where the new dataset should be saved
OUTPUT_FILE = BASE_DIR / "Clean Datasets" / "Cleaned Global Groundwater Monitoring Network dataset.csv"
# Finding "country" column in the dataset and filtering to have only "United States".
# Then save to a new CSV file.
df = pd.read_csv(DATA_FILE)
us_df = df[df["country"] == "United States"]
# Putting clean file in "Clean Datasets" folder and saving as a new CSV file.
us_df.to_csv(OUTPUT_FILE, index=False)
print(f"Cleaned file saved to: {OUTPUT_FILE}")

the code above was for limiting scope to US only"""

