import h5py

filepath = "MillionSongSubset/A/B/A/TRABACN128F425B784.h5"

with h5py.File(filepath, 'r') as f:
    song_metadata = f['metadata']['songs'][0]
    song_analysis = f['analysis']['songs'][0]

    print("Title:", song_metadata['title'].decode('utf-8'))
    print("Artist:", song_metadata['artist_name'].decode('utf-8'))
    print("Tempo:", song_analysis['tempo'])
    print("Loudness:", song_analysis['loudness'])
    print("Duration:", song_analysis['duration'])
    
