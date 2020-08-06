import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

# imports above let us access Spotify API through Python

# authorize us to make API calls using our credentials
# our credentials are stored as environment variables
# see https://developer.spotify.com/dashboard/applications
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# this will read in an argument or default to Taylor Swift
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Taylor Swift'

# get the artist URI to be used in the next part
results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
artist = items[0]
print(artist['name'])
uri = artist['uri']

# fetch the most popular tracks for you given artist
top_tracks = spotify.artist_top_tracks(uri)

# print the track name, link to audio preview, and cover art image
# for the artists top 5 songs
for track in top_tracks['tracks'][:5]:
    print('track:   : ' + track['name'])
    # had issue where some songs don't have preview audio, need to catch this!
    if track['preview_url'] is not None:
        print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
