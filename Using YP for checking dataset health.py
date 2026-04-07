# This file is re-used for most datasets hence the generic explanation

""" Using yp to check the "health" of the dataset.
    yp checks all values in your dataset (unless minimal = true for weaker hardware)
    and tries to find things like medians or means of a batch of values, checks for 
    inconsistencies in dates (if dates exist), and tries to find a correlation
    between remotely anything. After digging through the dataset, it generates 
    histograms for each variable so the distribution can be visualized. It also uses
    HTML to make the graphs interactive and makes data cleaning MUCH easier as you
    now know what batch of data is muddy.
    Using pathlib to make file management more easy.
"""

import pandas as pd
from ydata_profiling import ProfileReport
from pathlib import Path
# Finding working directory!
BASE_DIR = Path(__file__).parent
# Defining where the dataset is
DATA_FILE = BASE_DIR / "im3_open_source_data_center_atlas (data centers in US).csv"
# Getting file size in MB to determine how much yp should dig into the dataset
# .stat().st_size gets file size in bytes. We divide by 1024 twice to get it into MB.
FILE_SIZE_MB = DATA_FILE.stat().st_size / (1024 * 1024)
# Defining where the report should be saved
REPORT_DIR = BASE_DIR / "HTML reports by yp"
df = pd.read_csv(DATA_FILE)

""" "minimal" is an arguement that determines how much yp should dig into the dataset.
   The bigger the dataset, the less complex analysis yp does to save your hardware
  ".stem" cuts the file type and only gives the name of the file, eg instead of:
  "global_water_consumption_2000_2025.csv" it gives "global_water_consumption_2000_2025"
"""
# Check file size and automatically determine how much yp should dig into dataset.
# If file size is larger than 50MB, minimal = True that way the laptop doesn't crash,
# else minimal = False so we can squeeze as much information out of dataset as possible.
if FILE_SIZE_MB > 50:
    minimal = True
    print("Setting minimal = True")
else:
    minimal = False
    print("Setting minimal = False")
# Generate report and save it to Report directory.
profile = ProfileReport(df, title=f"Health Check for {DATA_FILE.stem}", minimal = minimal)
output_path = REPORT_DIR / f"{DATA_FILE.stem}_report.html"
profile.to_file(output_path)