# saveify
a small project to scrape songs on a Spotify playlist, searches them on YouTube, and downloads them. runs on Python 3.8+ and Windows 10.

# usage agreement
by using this, you agree to ONLY USE THIS TO DOWNLOAD PLAYLISTS YOU HAVE THE RIGHTS TO. i am NOT responsible if some DMCA guy knocks your front door because you decide to download the latest Justin Bieber hit.

# prerequirements
- have FFmpeg downloaded [(go here)](https://ffmpeg.org/download.html)
- have the following modules installed: *spotipy*, *mutagen*, *youtube_dl*
(to install: pip install spotipy, mutagen, youtube_dl)
- have a Spotify app with a Client ID and Client Secret [(make one)](https://developer.spotify.com/dashboard/applications)

# how to use
1) change **clientID** (Client ID) and **clientSecret** (Client Secret) to the one you have in your Spotify app
2) change **ffmpegDir** to where you downloaded FFmpeg (note: use the bin folder for the complete directory. for example: C:\FFmpeg\bin). i recommend to put this right on the C:\ or D:\ directory.
3) change **directory** to where you want the files to be downloaded. **DON'T USE SPACES!**
4) change **profileUri** to your Spotify profile URI.
6) change **playlistUri** to the playlist URI you want to download.
7) save and run!

# known bugs
- can't rename certain songs with special characters in them
- search method can be improved; it sometimes downloads full performances and shit lol
