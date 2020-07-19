import json
import requests
from secrets import spotify_user_id, spotify_token

# Create playlist
def create_playlist(artist):
    playlist_name = "The Anthology of " + artist
    request_body = json.dumps({
        "name": playlist_name,
        "description": "Every Song by Your Favorite Artist",
        "public": True
    })
    query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
    response = requests.post(
        query,
        data = request_body,
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    response_json = response.json()
    
    #playlist id
    return response_json["id"]

def search(artist):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        run_search_string(letter, artist)
    return

# Search for songs by artist, returns a list of uris with that search string
def run_search_string(search_string, artist):
    query = "https://api.spotify.com/v1/search?q={}&type=track&artist={}&market=US".format(
        search_string, artist.replace(" ", "%20")
    )
    response = requests.get(
        query,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    response_json = response.json()
    songs = response_json["tracks"]["items"]
    number_results = songs.size()
    for x in range(number_results):
        uri = songs[x]["uri"]
        add_song_to_playlist(uri)
    if (len(songs) == 50):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            run_search_string(search_string+letter, artist)
    return     

# Add song to the playlist
def add_song_to_playlist(uri):
    pass