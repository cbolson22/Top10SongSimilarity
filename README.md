### 1.
## Made this directory and added in the MillionSongSubset

### 2.
## Added a venv and installed dependencies
# > python3 -m venv venv
# > source venv/bin/activate
# > pip install -r requirements.txt

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
## After reviewing billboard.py, decided to use kaggle dataset instead: https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs
# Download as zip file and move "charts.csv" into your directory

### 8.
## Cleaned artist and song data, and merged:
# Remove punctuation, parenthesis
# For artists: remove songs with multiple collaborators so it can match MSD (which only has one artist)
# Merged and wrote to merged.csv

### 9. 
## Compute Weekly Averages:
# Since we have a small dataset, most weeks only have 1 or 2 songs. The full counts are here:
| # Songs in week| # Weeks |
|---|-------|
| 1 | 771   |
| 2 | 492   |
| 3 | 250   |
| 4 | 199   |
| 5 | 93    |
| 6 | 77    |
| 7 | 31    |
| 8 | 10    |
# For analysis we may want to only use weeks that have a certain amount of songs
# Overall, only 271 unique songs from the charts are found in the MSD subset, so figure out alternate data sources if necessary 