import pandas as pd
from pathlib import Path
# Finding working directory!
# .parent arguement makes it so it finds the folder in which this py file is in (our working directory) instead of just this file.
BASE_DIR = Path(__file__).parent
# Defining where the dataset is
DATA_FILE = BASE_DIR / "Raw Datasets" / "Cooling_Boiler_Generator_Data_Summary_2024.xlsx"
# Defining where the cleaned dataset should be saved
CLEANED_DATA_DIR = BASE_DIR / "Clean Datasets"
# Reading in dataset
df = pd.read_excel(DATA_FILE, header=2)

# Cleaning column names since excel file has weird spacing/newline issues in headers
df.columns = df.columns.str.strip()

print(df.columns)
# Keeping columns needed for analysis and dropping rest.
columns_to_keep = [
    "State", 
    "Plant Name", 
    "Year", 
    "Month", 
    "Generator Primary Technology", 
    "Net Generation from Steam Turbines (MWh)", 
    "Fuel Consumption from All Fuel Types (MMBTU)", 
    "Water Consumption Volume (Million Gallons)", 
    "Water Withdrawal Intensity Rate (Gallons / MWh)", 
    "Water Consumption Intensity Rate (Gallons / MWh)", 
    "Water Withdrawal Rate per Fuel Consumption (Gallons / MMBTU)", 
    "Water Consumption Rate per Fuel Consumption (Gallons / MMBTU)", 
    "Cooling Unit Hours in Service", 
    "Average Distance of Water Intake Below Water Surface (Feet)", 
    "Water Type", 
    "Water Source", 
    "Water Source Name", 
    "Water Discharge Name"
]
df = df[columns_to_keep]
# Remove rows where any of these columns have no value: Water Consumption Volume (Million Gallons),
# Water Withdrawal Intensity Rate (Gallons / MWh),
# Water Consumption Intensity Rate (Gallons / MWh), Water Withdrawal Rate per Fuel Consumption (Gallons / MMBTU),
# Water Consumption Rate per Fuel Consumption (Gallons / MMBTU)
# Could be either N/A or have " ", or be 0, so need to check for both N/A and " " as well as 0. First with replacing " " and 0 with nan:
# We should also remove negative values if they exist since it doesn't make sense to have negatives in this dataset. Replacing negatives with nan as well.

# Converting columns that should be numeric into numeric values, anything invalid becomes NaN automatically
numeric_columns = [
    "Net Generation from Steam Turbines (MWh)", 
    "Fuel Consumption from All Fuel Types (MMBTU)", 
    "Water Consumption Volume (Million Gallons)", 
    "Water Withdrawal Intensity Rate (Gallons / MWh)", 
    "Water Consumption Intensity Rate (Gallons / MWh)", 
    "Water Withdrawal Rate per Fuel Consumption (Gallons / MMBTU)", 
    "Water Consumption Rate per Fuel Consumption (Gallons / MMBTU)", 
    "Cooling Unit Hours in Service", 
    "Average Distance of Water Intake Below Water Surface (Feet)"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Replacing 0 and negative values with nan only for numeric columns so python doesn't choke when processing strings
df[numeric_columns] = df[numeric_columns].mask(df[numeric_columns] <= 0)

df = df.dropna(subset=[
    "Water Consumption Volume (Million Gallons)", 
    "Water Withdrawal Intensity Rate (Gallons / MWh)", 
    "Water Consumption Intensity Rate (Gallons / MWh)", 
    "Water Withdrawal Rate per Fuel Consumption (Gallons / MMBTU)", 
    "Water Consumption Rate per Fuel Consumption (Gallons / MMBTU)"])
print(df.head(40))
# By the look of the YP report, there are some MASSIVE outliers which we need to remove, gemini suggested clipping the top 1% so let's do that.
skewed_columns = [
    "Water Withdrawal Intensity Rate (Gallons / MWh)",
    "Water Consumption Intensity Rate (Gallons / MWh)",
    "Water Withdrawal Rate per Fuel Consumption (Gallons / MMBTU)",
    "Water Consumption Rate per Fuel Consumption (Gallons / MMBTU)"]

for column in skewed_columns:
    upper_limit = df[column].quantile(0.99)
    df = df[df[column] <= upper_limit]
print(df.head(40))
# Exporting cleaned dataset to Clean Datasets folder
output_path = CLEANED_DATA_DIR / "Cleaned Cooler_Boiler_Generator_Data_Summary_2024.csv"
df.to_csv(output_path, index=False)
print(f"Cleaned file saved to: {output_path}")
print(df.head())