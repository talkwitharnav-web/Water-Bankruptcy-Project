import pandas as pd
df = pd.read_csv("im3_open_source_data_center_atlas (data centers in US).csv")
print(len(df),"rows before editing anything")
""" If "operator", "ref", and "name" columns are all missing a value, drop that specific row.
    how='all' controls how strict pd is about dropping the row. If how='all', all columns must
    be missing a value for the row to be dropped. If how='any', then any row can be dropped if
    even one column is missing that value. We want only the row to be dropped if the data
    center cannot be identified.
"""
df = df.dropna(subset=["operator", "ref", "name"], how="all")
print(len(df),"rows after dropping rows with no form of identification")
# Now checking if "operator", "name", or both aren't N/A
has_operator = df["operator"].notna()
has_name = df["name"].notna()
# Now remove the row if it lacks operator and name
df = df[has_operator | has_name]
print(len(df),"rows after dropping rows with no operator and no name")