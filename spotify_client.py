from dataclasses import dataclass

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

@dataclass
class Playlist:
    name: str
    description: str
    tracks: list[str]

class SpotifyClient:

    def __init__(self) -> None:
        client_id = ""
        client_secret = ""
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.spotify = spotipy.Spotify(auth_manager=auth_manager)

    def get_playlist(self, id: str):
        playlist = self.spotify.playlist(id)
        """ second_hundred = self.spotify.user_playlist_tracks("spotify",id, offset=100)
        third_hundred = self.spotify.user_playlist_tracks("spotify",id, offset=200)
        fourth_hundred = self.spotify.user_playlist_tracks("spotify",id, offset=300)
        fifth_hundred = self.spotify.user_playlist_tracks("spotify",id, offset=400) """

        queries = []
        
        tracks = playlist['tracks']['items']
        #second_hundred_tracks = second_hundred['items']
        #third_hundred_tracks = third_hundred['items']
        #fourth_hundred_tracks = fourth_hundred['items']
        #fifth_hundred_tracks = fifth_hundred['items']
        
        for track in tracks:
            track_name = track['track']['name']
            artists = ', '.join([artist['name'] for artist in track['track']['artists']])
            queries.append(f'{track_name} by {artists}')

        """ for track in second_hundred_tracks:
            track_name = track['track']['name']
            artists = ', '.join([artist['name'] for artist in track['track']['artists']])
            queries.append(f'{track_name} by {artists}')

        for track in third_hundred_tracks:
            track_name = track['track']['name']
            artists = ', '.join([artist['name'] for artist in track['track']['artists']])
            queries.append(f'{track_name} by {artists}')

        for track in fourth_hundred_tracks:
            track_name = track['track']['name']
            artists = ', '.join([artist['name'] for artist in track['track']['artists']])
            queries.append(f'{track_name} by {artists}')

        for track in fifth_hundred_tracks:
            track_name = track['track']['name']
            artists = ', '.join([artist['name'] for artist in track['track']['artists']])
            queries.append(f'{track_name} by {artists}') """
        print(len(queries))
        return(Playlist(tracks['name'], tracks['description'], queries))
    

'''
IMPORTANT:
Un-comment the commented code only when you have more than 100 songs in the playlist you are trying to move to YT.
Spotify currently has a limit on number of tracks that can be fetched from a user's playlist using its API. (It is capped at 100 songs)
The commented code skips over the first 100 songs and fetches next 100, then next 100 and so on.
There may be a better way for this. I am currently unaware of that. If you find it, please do not hesitate to ping me.
'''
