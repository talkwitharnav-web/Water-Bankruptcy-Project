# Shutil is a library that lets us do file operations such as copy pasting (that is our use here)
import shutil
import pandas as pd
from pathlib import Path
# Since there are a lot of files, I am using tqdm to make a progress bar for my sanity.
# Not at all necessary but very helpful to know if the code is running or frozen.
from tqdm import tqdm
# Finding working directory!
# .parent arguement makes it so it finds the folder in which this py file is in (our working directory) instead of just this file.
BASE_DIR = Path(__file__).parent
# Defining where the dataset is
DATA_FILE = BASE_DIR / "USA - GGMN" / "monitoring"
# Defining where the clean dataset should be saved
CLEAN_DATASET_DIR = BASE_DIR / "Clean Datasets" / "USA - GGMN - CLEANED" / "monitoring"
# This makes a list for tqdm so it can knows how many files there are and accordingly make a progress bar
all_files = list(DATA_FILE.glob("*.ods"))
""" We loop through all the files one at a time, with filepath holding the path of the file. The tqdm part is a wrapper so it can use our list and update progress, giving
    stats like how many files are left, how much time is remaining, and the speed of processing.
    Also unit="file" just tells tqdm that instead of displaying rate of progress as "it/s" (iterations per second)
    it should display as "file/s" so it's just more readable.
"""
for filepath in tqdm(all_files, unit="file"):
    # try catch block for safety
    try:
        df = pd.read_excel(filepath,
                           engine = "odf" # ods isn't typically readable by pandas so specifying engine is necessary
                           , header= None # no headers in these files
                           , nrows = 2 # only want first two rows
                           )
        # Converting the specified cell to text and using if block
        if str(df.iloc[0,1]).strip().lower() == "name":
            # If the cell does contain "name", we copy paste it because we need location in our fileset, also copy2 preserves EVERYTHING raw
            shutil.copy2(filepath, CLEAN_DATASET_DIR / filepath.name)
    except:
        # If file doesn't cooperate, skip it
        pass

