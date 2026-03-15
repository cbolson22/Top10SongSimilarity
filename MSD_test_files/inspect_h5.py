import h5py

filepath = "MillionSongSubset/A/A/A/TRAAAAW128F429D538.h5"

with h5py.File(filepath, 'r') as f:
    print("Top-level keys:", list(f.keys()))

    for key in f.keys():
        print(f"\nInspecting group: {key}")
        print(list(f[key].keys()))