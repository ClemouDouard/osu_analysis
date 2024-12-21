import pandas as pd

df = pd.read_csv('data/raw/metadata.csv', index_col='beatmapset_id')

cols_to_drop = ['split', 'Unnamed: 0', 'audio_hash', 'file_md5', 'beatmap_id', 'source', 'tags', 'artist_unicode', 'title_unicode', 'packs']

df.drop(cols_to_drop, axis=1, inplace=True)

df = df.dropna(subset=['version'])
df = df.dropna(subset=['artist'])
df = df.dropna(subset=['title'])
df = df.dropna(subset=['max_combo'])

df['max_combo'] = df['max_combo'].astype(int)
df['submit_date'] = pd.to_datetime(df['submit_date'])
df['approved_date'] = pd.to_datetime(df['approved_date'])
df['last_update'] = pd.to_datetime(df['last_update'])

df_withoutdiffaimspeed = df.copy()
df_withoutdiffaimspeed.drop(['diff_aim', 'diff_speed'], axis=1, inplace=True)

df_withdiffaimspeed = df.dropna(subset=['diff_aim'])
df_withdiffaimspeed = df_withdiffaimspeed.dropna(subset=['diff_speed'])

df_withdiffaimspeed.to_csv('data/interim/withdiff.csv', index='beatmapset_id')
df_withoutdiffaimspeed.to_csv('data/interim/withoutdiff.csv', index='beatmapset_id')