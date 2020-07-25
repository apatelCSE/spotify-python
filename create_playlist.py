import json
import requests
from secrets import spotify_user, spotify_token_id

class CreatePlaylist:
    def __init__(self, artist):
        self.song_uris = []
        self.artist = artist
        self.spotify_user_id = spotify_user
        self.spotify_token = spotify_token_id

    def create_playlist(self):
        playlist_name = "The Anthology of " + self.artist
        request_body = json.dumps({
            "name": playlist_name,
            "description": "Every Song by Your Favorite Artist",
            "public": True
        })
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.spotify_user_id)
        response = requests.post(
            query,
            data = request_body,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )
        response_json = response.json()
        
        #playlist id
        return response_json["id"]

    def search(self):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            self.run_search_string(letter)
        return

    # Search for songs by artist, returns a list of uris with that search string
    def run_search_string(self, search_string):
        query = "https://api.spotify.com/v1/search?q={}&type=track&artist={}&market=US".format(
            search_string, self.artist.replace(" ", "%20")
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]
        number_results = songs.size()
        for x in range(number_results):
            uri = songs[x]["uri"]
            self.song_uris.add(uri)
        if (len(songs) == 50):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                self.run_search_string(search_string+letter)
        return  

    # Add song to the playlist
    def add_song_to_playlist(self):
        # create new playlist
        playlist_id = self.create_playlist()

        #add songs to new playlist
        request_data = json.dumps(uris)

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )
        response_json = response.json()
        return response_json