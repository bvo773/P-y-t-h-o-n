import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

client_id = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]

credentials = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=credentials)

user = spotify.user('1274462219')
print(user)

print()

'''
def create_playlist():
  user_id = input("User ID: ")
  playlist_name = input("Playlist name: ")
  description = "Playlist created from spotifyapi"
  spotify.user_playlist_create(user_id, playlist_name, True, False, description)
'''
def main():
  #create_playlist()

if __name__ == "__main__":
  main()
