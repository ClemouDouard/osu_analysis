# Osu 
Osu is a rythm game where the goal is to click circles to the beat.
All of the beatmaps are made by the community and are free to download.

The goal here is to make some statistics and visualizations about those beatmaps, and find correlation between variables.

## Data

The [data](https://www.kaggle.com/datasets/alumkal/osu-beatmaps) is from Kaggle. It contains more than 100 000 rows, and has 44 columns :

- `split` :
- `audio_hash` :
- `beatmap_id` : The id of the beatmap.
- `approved` : 1 if the map is in an approved state, 0 otherwise.
- `total_length` : Total length of a beatmap in seconds.
- `hit_length` : Total length minus the length of the breaks in seconds.
- `version` : The version/mapset of the beatmap.
- `file_md5` :
- `diff_size` : The size of the circles.
- `diff_overall` : The precision required to click in time a circle.
- `diff_approach` : The approach rate.
- `diff_drain` : The drain rate.
- `mode` : The mode of the beatmap (osu, taiko, catch, mania).
- `count_normal` : The number of circles.
- `count_slider` : The number of sliders.
- `count_spinner` : The number of spinners.
- `approved_date` : The date the map was approved.
- `last_update` : The date the map was last updated.
- `artist` : The artist of the song.
- `artist_unicode` : The artist of the song in unicode.
- `title` : The title of the song.
- `title_unicode` : The title of the song in unicode.
- `creator` : The creator of the map.
- `creator_id` : The id of the creator.
- `bpm` : The BPM of the song.
- `source` : 
- `tags` : The tags of the beatmapset
- `genre_id` : The id of the genre of the song.
- `language_id` : The id of the language of the song.
- `favourite_count` : The number of times the map was favourited.
- `rating` : The rating of the map from 0 to 10.
- `storyboard` : 1 if the map has a storyboard, 0 otherwise.
- `video` : 1 if the map has a video, 0 otherwise.
- `download_unavailable` : 1 if the map is not downloadable, 0 otherwise.
- `audio_unavailable` : 1 if the audio is not available, 0 otherwise.
- `playcount` : The number of times the map was played.
- `passcount` : The number of times the map was passed.
- `packs` : The number of packs the map is in.
- `max_combo` : The maximum combo possible.
- `diff_aim` : The aim difficulty in the overall difficulty.
- `diff_speed` : The speed difficulty in the overall difficulty.
- `difficultyrating` : The difficulty rating of the map.

