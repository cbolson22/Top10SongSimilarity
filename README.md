### 1.
## Made this directory and added in the MillionSongSubset

### 2.
## Added a venv and installed dependencies
# > python3 -m venv venv
# > source venv/bin/activate
# > pip install pandas numpy h5py billboard.py

### 3.
## Ran the inspect_h5.py file to see how the .h5 files are structures
# > python inspect_h5.py

### 4.
## Ran the extract_one.py file to see the values of a .h5 file print out correctly
# > python extract_one.py

### 5.
## Ran the build_subset_table.py file to build the csv with basic info for now (can expand the fields we want to include too)
# > python build_subset_table.py

### 6.
## Ran the inspect_subset.py file to print out some basic things about the csv to check it\
# > python inspect_subset.py
# looks good I think (can probably delete danceability and energy tho)

### 7.
## Started running the build_billboard_table.py file to make the csv for top 10 songs, but WAS TAKING WAY TOO LONG (10 seconds per week)
## IS THERE A BETTER WAY TO EXTRACT FROM BILLBOARD.py??
# > python build_billboard_table.py


### TODO
## 1. Quick check on the billboard csv to make sure it looks good

## 2. CLEAN NAMES???
# EXAMPLE:
<!-- import re

def clean_string(s):
    s = s.lower()
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'[^a-z0-9 ]', '', s)
    return s.strip()

df_msd["clean_title"] = df_msd["title"].apply(clean_string)
df_billboard["clean_title"] = df_billboard["title"].apply(clean_string) -->


## 3. Merge DFs together
# EXAMPLE:
<!-- df_merged = pd.merge(
    df_billboard,
    df_msd,
    left_on="clean_title",
    right_on="clean_title",
    how="inner"
) -->


## 4. Compute Weekly Averages (if have time before first meeting) and turn df into merged CSV
# EXAMPLE:
<!-- features = ["tempo", "loudness", "key", "mode"]

df_weekly = (
    df_merged
    .groupby("week")[features]
    .mean()
    .reset_index()
)

# Save full merged df to csv
df_weekly.to_csv("weekly_top10_centroids.csv", index=False) -->

## 5. Examine for any obvious errors