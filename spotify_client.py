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
        first_hundred = self.spotify.playlist(id)
        second_hundred = self.spotify.user_playlist_tracks("spotify",id, offset=100)
        third_hundred = self.spotify.user_playlist_tracks("spotify",id, offset=200)
        fourth_hundred = self.spotify.user_playlist_tracks("spotify",id, offset=300)
        fifth_hundred = self.spotify.user_playlist_tracks("spotify",id, offset=400)

        queries = []
        
        first_hundred_tracks = first_hundred['tracks']['items']
        second_hundred_tracks = second_hundred['items']
        third_hundred_tracks = third_hundred['items']
        fourth_hundred_tracks = fourth_hundred['items']
        fifth_hundred_tracks = fifth_hundred['items']
        
        for track in first_hundred_tracks:
            track_name = track['track']['name']
            artists = ', '.join([artist['name'] for artist in track['track']['artists']])
            queries.append(f'{track_name} by {artists}')

        for track in second_hundred_tracks:
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
            queries.append(f'{track_name} by {artists}')
        print(len(queries))
        return(Playlist(first_hundred['name'], first_hundred['description'], queries))
    
# test
""" spotify = SpotifyClient()
spotify.get_playlist("") """