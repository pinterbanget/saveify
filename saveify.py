import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import subprocess
import time
import os
from mutagen.easymp4 import EasyMP4
from youtube_dl import YoutubeDL

#YOU ONLY WANT TO CHANGE THINGS BELOW THIS
clientId = 'dqw4w9wgxcq' #change with your Client ID from Spotify app
clientSecret = 'd1YBv2mWll0' #change with your Client Secret from Spotify app
directory = r"D:\blablabla\yaddayadda" #change with your destination directory. don't use spaces
ffmpegDir = r"D:\FFmpeg\bin" #change with your FFmpeg directory. don't use spaces
username = '085700088839' #change with your Spotify username.
playlistUri = 'spotify:playlist:0RGOFtQCYhoPnzZdhRcgpQ' #change with your Spotify playlist URI.
#YOU ONLY WANT TO CHANGE THINGS ABOVE THIS

clientCredents = SpotifyClientCredentials(client_id = clientId, client_secret = clientSecret)
sp = spotipy.Spotify(client_credentials_manager = clientCredents)

def getSongTitle(uri):
    global playlistName, songList, playlistTitles, playlistArtists, playlistDurations
    
    playlistId = uri.split(':')[2]
    playlist = sp.user_playlist(username, playlistId)
    
    playlistData = playlist['tracks']
    playlistName = playlist['name']
    playlistTitles = []
    playlistArtists = []
    playlistFeatures = [] #gabakal kepake
    playlistDurations = [] 

    for track in playlistData['items']:
        playlistTitles.append(track['track']['name'])
        artistList = []
        for artist in track['track']['artists']:
            artistList.append(artist['name'])
        playlistArtists.append(artistList[0])
        playlistFeatures.append(artistList)
        playlistDurations.append(track['track']['duration_ms'])
    
    songList = []
    for i in range(len(playlistTitles)):
        songList.append(playlistArtists[i] + ' ' + playlistTitles[i])
    
    downloadSongs(songList)

def downloadSongs(songList):
    subprocess.Popen('cd {} & mkdir "{}"'.format(directory, playlistName), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    time.sleep(1)
    os.chdir(r'{}\{}'.format(directory, playlistName))
    
    for i in range (len(songList)):
        fileName = playlistArtists[i] + ' - ' + playlistTitles[i]
        if os.path.exists('{}.m4a'.format(fileName)):
            print('{} already exists!'.format(fileName))
            continue
        
        #duration filter doesn't work. todo: make a filter that matches duration of video downloaded with the Spotify length, maybe put (+-)3s tolerance
        duration = int(playlistDurations[i])/1000
        ydl = YoutubeDL({'ffmpeg_location': '{}'.format(ffmpegDir), 'format': 'bestaudio[ext=m4a]', 'matchfilter': 'duration < {}'.format(str(duration+5)), 'noplaylist': 'True', 'postprocessors': [{'key': 'FFmpegExtractAudio'}]})
        info = ydl.extract_info('ytsearch:{} audio'.format(songList[i]), download = True)['entries'][0]
        
        try:
            os.rename('{}-{}.m4a'.format(info['title'], info['id']), '{}.m4a'.format(fileName))
        except OSError:
            print("Can't rename {}!".format(info['title']))
            continue
            
        metatag = EasyMP4('{}.m4a'.format(fileName))
        metatag['title'] = playlistTitles[i]
        metatag['artist'] = playlistArtists[i]
        metatag['album'] = playlistName
        metatag.save()

if __name__ == '__main__':
    getSongTitle(playlistUri)
