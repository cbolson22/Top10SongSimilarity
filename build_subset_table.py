import os
import h5py
import pandas as pd

base_path = "MillionSongSubset"
rows = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".h5"):
            filepath = os.path.join(root, file)

            try:
                with h5py.File(filepath, 'r') as f:
                    metadata = f['metadata']['songs'][0]
                    analysis = f['analysis']['songs'][0]

                    row = {
                        "track_id": analysis['track_id'].decode('utf-8'),
                        "song_id": metadata['song_id'].decode('utf-8'),
                        "title": metadata['title'].decode('utf-8'),
                        "artist_name": metadata['artist_name'].decode('utf-8'),

                        "tempo": analysis['tempo'],
                        "loudness": analysis['loudness'],
                        "duration": analysis['duration'],
                        "danceability": analysis['danceability'],
                        "energy": analysis['energy'],
                        "key": analysis['key'],
                        "mode": analysis['mode'],
                        "time_signature": analysis['time_signature'],
                    }

                    rows.append(row)

            except Exception as e:
                print(f"Error reading {filepath}: {e}")

df = pd.DataFrame(rows)

print("Total songs processed:", len(df))
df.to_csv("msd_subset_metadata.csv", index=False)