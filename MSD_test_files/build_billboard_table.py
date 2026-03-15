import pandas as pd

# Read in CSVs
df_msd = pd.read_csv("msd_subset_metadata.csv", sep=",") 
df_billboard = pd.read_csv("charts.csv", sep=',')

# Clean song data
def clean_song(s: pd.Series) -> pd.Series:
    return (s.str.lower()
             .str.replace(r'\(.*?\)', '', regex=True)
             .str.replace(r'[^a-z0-9 ]', '', regex=True)
             .str.strip())

# Clean artist data (some features weren't matching)
def clean_artist(s: pd.Series) -> pd.Series:
    return (s.str.lower()
             .str.replace(r'\(.*?\)', '', regex=True)
             .str.replace(r'featuring.*', '', regex=True)
             .str.replace(r' ft\..*', '', regex=True)
             .str.replace(r' x .*', '', regex=True)
             .str.split('&').str[0]
             .str.replace(r'[^a-z0-9 ]', '', regex=True)
             .str.strip())

# Clean
df_billboard["clean_song"]   = clean_song(df_billboard["song"])
df_msd["clean_title"]  = clean_song(df_msd["title"])

df_billboard["clean_artist"] = clean_artist(df_billboard["artist"])
df_msd["clean_artist"]       = clean_artist(df_msd["artist_name"])

# Merge
df_merged = df_billboard.merge(
    df_msd,
    left_on=["clean_song", "clean_artist"],
    right_on=["clean_title", "clean_artist"],
    how="inner"
)

# Stats
print(f"Billboard rows: {len(df_billboard)}")
print(f"Matched rows:   {len(df_merged)}")
print(f"Unmatched:      {len(df_billboard) - len(df_merged)}")
print(f"Unique songs:   {df_merged['song'].nunique()}")

# Write merged CSV
df_merged.to_csv("merged.csv", index=False)

features = ["tempo", "loudness", "key", "mode"]

# Group by week
df_weekly = (
    df_merged
    .groupby("date")
    .agg(
        {f: "mean" for f in features} | {"track_id": "count"}
    )
    .rename(columns={"track_id": "count"})
    .reset_index()
)
df_weekly = df_weekly.sort_values(by=["count"])
print(df_weekly)
print(df_weekly['count'].value_counts())
df_weekly.to_csv("weekly_top10_centroids.csv", index=False)