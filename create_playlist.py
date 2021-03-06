import json
import math
import requests
from secrets import spotify_user, spotify_token_id

print("Hello world!")

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
        for letter in "abcdefghijklmnopqrstuvwxyz1234567890":
            self.run_search_string(letter, 0)
        return

    # Search for songs by artist, returns a list of uris with that search string
    def run_search_string(self, search_string, offset):
        query = "https://api.spotify.com/v1/search?q=track:{}%20artist:{}&type=track&market=US&limit=50&offset={}".format(
            search_string, self.artist.replace(" ", "%20"), offset
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
        number_results = len(songs)
        for x in range(number_results):
            uri = songs[x]["uri"]
            artists = songs[x]["artists"]
            correct_artist = False
            for artist_index in range(len(artists)):
                artist_name = artists[artist_index]["name"]
                if (artist_name == self.artist):
                    correct_artist = True
            unique_uri = uri not in self.song_uris
            if (correct_artist and unique_uri):
                self.song_uris.append(uri)
        if (len(songs) == 50):
            if (offset < 1950):
                self.run_search_string(search_string, offset + 50)
            else:
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    self.run_search_string(search_string+letter, 0)
        return  

    # Make add_to_playlist query
    def make_query(self, playlist_id, array):
        request_data = json.dumps(array)

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


    # Add song to the playlist
    def add_song_to_playlist(self):
        # create new playlist
        playlist_id = self.create_playlist()

        #add songs to new playlist
        self.search()
        number_of_queries = math.ceil(len(self.song_uris) / 100)
        for i in range(number_of_queries):
            self.make_query(playlist_id, self.song_uris[i*100:(i+1)*100])

if __name__ == '__main__':
    artist = input("Enter artist name: ")
    cp = CreatePlaylist(artist)
    cp.add_song_to_playlist()