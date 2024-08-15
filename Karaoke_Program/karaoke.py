# Prompting the User to enter File Path and Song Name:

from begin import get_file_path, get_song_title

audio_file_path = get_file_path("Please enter the path to the audio file: ")
song_title = get_song_title("Please enter the title of the song: ")

# Creating Lyrics File With TimeStamps:

print("*\n*\n*\n*\n*\nCreating Lyrics File With Time Stamps\n*\n*\n*\n*\n*")

from lyrics_timestamps import transcribe_audio_with_detailed_timestamps

lyrics_all_timestamps = transcribe_audio_with_detailed_timestamps(audio_file_path)

# Receiving Pictures Based On the Lyrics with TimeStamps using DALL-E API

print("*\n*\n*\n*\n*\nReceiving Pictures Based On the Lyrics with TimeStamps using DALL-E API\n*\n*\n*\n*\n*")

import openai_init

from pict import extract_text_segments_from_result, get_images_urls, download_images

text_segments = extract_text_segments_from_result(lyrics_all_timestamps)

image_urls = get_images_urls(text_segments)

slide_pictures = download_images(image_urls, song_title)

# Separating the Vocals to get the Instrumental Audio Version

print("*\n*\n*\n*\n*\nSeparating the Vocals to get the Instrumental Audio Version\n*\n*\n*\n*\n*")

from sepa import separate_audio_with_demucs

instrumental = separate_audio_with_demucs(audio_file_path)

# Creating Video with Audio and Slide Show using generated Images

print("*\n*\n*\n*\n*\nCreating Video with Audio and Slide Show using generated Images\n*\n*\n*\n*\n*")

from first_video import extract_number, create_video_from_images_and_audio

video_without_lyrics = create_video_from_images_and_audio(slide_pictures, instrumental, lyrics_all_timestamps, song_title, fps=24)

# Creating Karaoke Video by adding the lyrics to video_without_lyrics

print("*\n*\n*\n*\n*\nCreating Karaoke Video by adding the lyrics\n*\n*\n*\n*\n*")

from final_video import wrap_text, create_video_with_highlighted_text

karaoke_video = create_video_with_highlighted_text(video_without_lyrics, song_title, lyrics_all_timestamps)

print("*\n*\n*\n*\n*\nKaraoke Video is ready to play!\n*\n*\n*\n*\n*")