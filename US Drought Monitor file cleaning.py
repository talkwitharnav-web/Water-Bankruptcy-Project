import pandas as pd
from pathlib import Path
# Finding working directory!
# .parent arguement makes it so it finds the folder in which this py file is in (our working directory) instead of just this file.
BASE_DIR = Path(__file__).parent
# Defining where the dataset is
DATA_FILE = BASE_DIR / "Raw Datasets" / "US Drought Monitor (all states, categorical, percent of area).csv"
# assigning csv to dataframe
df = pd.read_csv(DATA_FILE)
print(df.head())
""" D0: Abnormally Dry
    D1: Moderate Drought
    D2: Severe Drought
    D3: Extreme Drought
    D4: Exceptional Drought"""
# Replacing abbreviations of states with full names for powerbi (reference: https://www.50states.com/abbreviations.htm)
df["StateAbbreviation"] = df["StateAbbreviation"].replace({
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
})
# Rename State column
df = df.rename(columns={"StateAbbreviation": "State"})
# Exporting into Cleaned Datasets folder
df.to_csv(BASE_DIR / "Clean Datasets" / "Cleaned US Drought Monitor dataset.csv", index=False)
print(f"Cleaned file saved to: {BASE_DIR / 'Clean Datasets' / 'Cleaned US Drought Monitor dataset.csv'}")
print(df.head())
