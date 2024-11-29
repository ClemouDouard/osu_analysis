import pandas as pd

df = pd.read_csv('data/raw/metadata.csv', index_col='beatmapset_id')

cols_to_drop = ['split', 'Unnamed: 0', 'audio_hash', 'file_md5', 'beatmap_id', 'source', 'tags']

df.drop(cols_to_drop, axis=1, inplace=True)

print(df.head())