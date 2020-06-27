import json
import requests
from secrets import spotify_user_id, spotify_token

class CreatePlaylist:
    def __init__(self, name):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
    
    # Create playlist
    def create_playlist(self, name):
        playlist_name = "The Anthology of " + name
        request_body = json.dumps({
            "name": playlist_name,
            "description": "Every Song by Your Favorite Artist",
            "public": True
        })
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
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

    # Search for songs by artist
    def get_spotify_uri(self):
        pass

    # Add song to the playlist
    def add_song_to_playlist(self):
        pass