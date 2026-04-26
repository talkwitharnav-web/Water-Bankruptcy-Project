import pandas as pd
from pathlib import Path
# Finding working directory!
# .parent arguement makes it so it finds the folder in which this py file is in (our working directory) instead of just this file.
BASE_DIR = Path(__file__).parent
# Defining where the dataset is
DATA_FILE = BASE_DIR / "Raw Datasets" / "USDA NASS SPREADSHEET.csv"
# assigning csv to dataframe
df = pd.read_csv(DATA_FILE)
print(df.head())


# Dropping rows that contain either "(D) or (H)" in the value or cv column
# We do this by making a mask (true or false value for each row), using that mask we filter out the true rows and keep false
# We check if (D) OR (H) is in the strings of both columns
mask = (
    df['Value'].astype(str).str.contains(r'\(D\)|\(H\)', na=False) | 
    df['CV (%)'].astype(str).str.contains(r'\(D\)|\(H\)', na=False)
)

# Update the dataframe by keeping only rows NOT in the mask (~)
# Reset index to be safe and drop the old index since we are removing rows
df = df[~mask].reset_index(drop=True)

print (df.head(30))

# Now we want to drop useless columns, which are ag district, ag district code, county, county ansi, zip code, region, and watershed_code, as well as Week Ending + Commodity
# We do this via drop function and specify columns we wanna drop and axis = 1 since we are dropping columns not rows
df = df.drop(columns=['Ag District', 'Ag District Code', 'County', 'County ANSI', 'Zip Code', 'Region', 'watershed_code', 'Week Ending', 'Commodity', 'State ANSI'])
print(df.head())

# Now the issue is that our watershed column holds some state names for some reason, so we want to merge those
# presumably state names into the state column and then drop the watershed column. First we need to find
# the row index of last value in states and row index of first value in watershed so we can merge.
last_index_state = df['State'].last_valid_index()
print(last_index_state)
first_index_watershed = df['Watershed'].first_valid_index()
print(first_index_watershed)
# Now we want to find the last row of information overall to know where to stop
last_index_overall = df.index[-1]
print(last_index_overall)
# Now we merge the watershed names into the states columns only AFTER the LAST VALUE in the states column
# But we also have to merge up till last overall index
df.loc[last_index_state + 1 : last_index_overall, 'State'] = df.loc[last_index_state + 1 : last_index_overall, 'Watershed']
# Now that it is done, we can drop the watershed column and export
df = df.drop(columns=['Watershed'])
# Remove any potential duplicate rows
df = df.drop_duplicates()
# Exporting into Cleaned Datasets folder
df.to_csv(BASE_DIR / "Clean Datasets" / "Cleaned USDA NASS dataset.csv", index=False)
print(f"Cleaned file saved to: {BASE_DIR / 'Clean Datasets' / 'Cleaned USDA NASS dataset.csv'}")
print(df.head(30))