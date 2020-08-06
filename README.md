# BuiltByGirlsSpotifyAPIExample
Example of using an API for Built By Girls [WAVE Mentorship](https://www.builtbygirls.com/about-wave) August 2020. 

This
is a simple project that will take in an artist name as an argument (or by default use our girl 
[TSwift](https://www.youtube.com/watch?v=nfWlot6h_JM)) and retrieve information on that artist's top 5 songs.

**Project Goals**
1. Understand the power an API gives you
1. Create an application and generate/use API keys
1. Brainstorm what else we could do with the Spotify API

## Review: What is an API?
- WATCH [this video](https://www.youtube.com/watch?v=s7wmiS2mSXY&feature=emb_title) on what an API is 
and what it helps you to do
- READ [this article](https://medium.com/@mandeepkaur1/what-is-an-api-and-why-are-they-important-to-developers-98ad18d45b93)
on why APIs are so important to developers 

## Getting Started 
### Dependencies

`python3` - make sure you have python installed (and an IDE you like such as PyCharm)

`spotipy` - get with `pip install spotipy` and [check out the docs](https://spotipy.readthedocs.io/en/2.13.0/#)

### Getting Spotify API Keys 

1. Go to [https://developer.spotify.com/](https://developer.spotify.com/) and log in with your Spotify account
1. Create a new application to get the Client ID and Client Secret
1. I copied my credentials into a `.env` file and used the `$ export` Unix command to be able to easily access and use them. 
(In an IDE like Pycharm you will have to go to Run > Edit Configurations to add them for use in the IDE)

### Authorization 

For more info on the `spotipy` authorization
[read the docs](https://spotipy.readthedocs.io/en/2.13.0/#authorization-code-flow) :)

```buildoutcfg
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
```
As stated above, make sure you use them as environmental variables so that they do not have to be hard-coded 
into your python code!
 
In the words of [Twilio](https://www.twilio.com/blog/2017/11/hardcoded-keys.html), *"If a developer exposes those keys 
into the public, someone can come along and access that developer’s Twilio account. It’s like leaving your car keys in 
an unlocked car — once someone realizes you’ve made the mistake they can drive your car wherever they want."*

## Doing More 

### Resources
- Spotipy Documentation: https://spotipy.readthedocs.io/en/2.13.0/#
- Spotify API Documentation: https://developer.spotify.com/documentation/web-api/

### Sample Projects
- [Mangomoji](http://www.mangomoji.com/) - Chooses a song for you based on emojis
- [Six Degrees of Kanye West](http://sixdegreesofkanyewest.com/) - "How close is your favorite artist to Yeezy?"
- [Acrostify](https://github.com/plamere/enspex/tree/master/web/Acrostify) - Make a playlist with an acrostic message 
hidden in the songs
- [Boil the Frog](https://github.com/plamere/BoilTheFrog) - "creates seamless Spotify playlists between any two artists"
- [and more!](https://developer.spotify.com/community/showcase/)

