# Karaoke-Project
![Alt text](<EDA Karaoke/README img/1696719209263-770387473SKY1V1.webp>)

This repository contains:

1. A program that creates an individual Karaoke video
2. An analysis of what makes a good Karaoke song.

### Karaoke Machine

The Goal of the Karaoke Machine is to create a full Karaoke Video, only by providing the audio file from the user.

Installation:

1. Clone this repository: (https://github.com/SeppiBrocki/Karaoke-Machine/tree/main/Karaoke%20Program)

2. Install (additional) libraries:

- NumPy
- MoviePy
- PyTorch
- Pillow
- whisper
- requests
- openAI (including API Key which can be stored in an .env file)
- dotenv

3. Run karaoke.py from your terminal - The Karaoke Video will be stored in the same directory

### EDA Karaoke - What makes a good Karaoke song?

In this analysis the Top 100 most streamed songs from spotify are compared to the Top 100 Karaoke songs. The Top 100 Karaoke songs are provided by this site: (https://www.singtotheworld.com/blog/100-most-popular-karaoke-songs-of-all-time). The Top 100 most streamed songs from Spotify are available as a Spotify Playlist or through this site: (https://kworb.net/spotify/songs.html).

The two playlists are compared by their track and audio features, which are available through the Spotify API.

#### Findings:

Below are listed the distributions for the metrics where a statistical significant difference was found:

![Alt text](<EDA Karaoke/README img/Bildschirmfoto 2024-08-15 um 21.26.09.png>)

![Alt text](<EDA Karaoke/README img/Bildschirmfoto 2024-08-15 um 21.26.30.png>)

![Alt text](<EDA Karaoke/README img/Bildschirmfoto 2024-08-15 um 21.26.45.png>)

![Alt text](<EDA Karaoke/README img/Bildschirmfoto 2024-08-15 um 21.27.19.png>)

![Alt text](<EDA Karaoke/README img/Bildschirmfoto 2024-08-15 um 21.27.33.png>)
