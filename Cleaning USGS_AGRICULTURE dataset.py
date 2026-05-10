import pandas as pd
from pathlib import Path
# Finding working directory!
# .parent arguement makes it so it finds the folder in which this py file is in (our working directory) instead of just this file.
BASE_DIR = Path(__file__).parent
# Defining where the dataset is
DATA_FILE = BASE_DIR / "Raw Datasets" / "USGS_AGRICULTURE_DATASET.csv"
# Defining where the cleaned dataset should be saved
CLEANED_DATA_DIR = BASE_DIR / "Clean Datasets"
# Reading in dataset
df = pd.read_csv(DATA_FILE)
# Keeping columns that are needed for analysis
columns_to_keep = ["STATE",
                   "COUNTY",
                   "YEAR",
                   "Public_Supply_GW",
                   "Public_Supply_SW",
                   "Public_Supply",
                   "Industrial_GW",
                   "Industrial_SW",
                   "Industrial",
                   "Irrigation_GW",
                   "Irrigation_SW",
                   "Irrigation",
                   "County_Standardized"
                   ]
df = df[columns_to_keep]
print(df.head(50))
# Now we want to remove rows where columns have missing values for example say:
# if "Public_Supply_GW" is missing a value but the SW has a value and then "Public_Supply" has a value,
# we can keep that row because it's accurate, whereas if both columns (GW and SW) were 0 and then "Public_Supply" were
# 0, then we remove it since it's useless. We have to do this for all three categories we're keeping.
# Removing rows with either a value of 0 or N/A in the three categories (Public Supply, Industrial, Irrigation)
df = df.dropna(subset=["Public_Supply_GW", "Public_Supply_SW", "Public_Supply",
                                "Industrial_GW", "Industrial_SW", "Industrial",
                                "Irrigation_GW", "Irrigation_SW", "Irrigation"])
# "~" is a NOT operator, so we are keeping rows that DO NOT have a 0 in all three columns specified
df = df[~((df["Public_Supply_GW"] ==0) & (df["Public_Supply_SW"]==0) & (df["Public_Supply"] == 0))]
print(df.head(50))
df = df[~((df["Industrial_GW"] ==0) & (df["Industrial_SW"]==0) & (df["Industrial"] == 0))]
print(df.head(50))
df = df[~((df["Irrigation_GW"] ==0) & (df["Irrigation_SW"]==0) & (df["Irrigation"] == 0))]
print(df.head(50))
# Saving cleaned dataset to Clean Datasets folder
output_path = CLEANED_DATA_DIR / "Cleaned USGS_AGRICULTURE_DATASET.csv"
df.to_csv(output_path, index=False)
print(f"Cleaned file saved to: {output_path}")
print(df.head())

