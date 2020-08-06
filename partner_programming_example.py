import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# imports above let us access Spotify API through Python

# authorize us to make API calls using our credentials
# our credentials are stored as environment variables
# see https://developer.spotify.com/dashboard/applications
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# GOAL: ????

# STEP 1: ???
