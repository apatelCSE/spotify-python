The Anthology of...
===================

A script that takes every song ever released by your favorite artist and creates a Spotify playlist filled with their works.

How to Run on Your Device
-------------------------
1. Download the source code under "Code".
2. Install the latests requests dependency by running ```pip install requests``` pip install requests on the command line (or your machine's equivalent).
3. Load your Spotify User ID and Oauth Token from Spotify into the secrets.py file. Don't forget to save the changes!
    - To Collect your User ID, Log into spotify.com then go here: [Account Overview](https://www.spotify.com/us/account/overview/) copy your Username.
    - To Collect your Oauth Token, go here: [Get Oauth](https://developer.spotify.com/console/post-playlists/) and click the **Get Token** button. Copy the token value.
4. Run ```python create_playlist.py``` in the project folder on the command line (you will need to navigate to the place where you stored the source code files).
