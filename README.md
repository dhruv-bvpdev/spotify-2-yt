# Spotify to YT

Move Spotify playlist to Youtube Music using Python and Youtube Data V3 API

## Spotify Client Secret

1. Login to your [Spotify Developer Account](https://developer.spotify.com/).
2. Navigate to dashboard and then click create app.
3. Fill out basic information about your app like name and description.
4. In the redirect URI textbox, enter `http://localhost:8080`
5. Check the Web API option.
6. Agree to the terms & conditions and click on save.
7. Naviagte to settings of your app and copy client ID and client secret.
8. Paste it in spotify_client.py file.

## YouTube Client Secret

1. Go to the Google Cloud Console, sign in with your Google account, and create a new project.
2. Once your project is created, select it from the project dropdown menu in the top navigation bar.
3. Click on the API & Services section in the left sidebar and navigate to Credentials page.
4. Click on the "Create Credentials" button and select "OAuth client ID".
5. At this point, you might be prompted to create an Auth Consent Screen if not already configured.
6. While creating the client ID, enter `http://localhost:8080` under the 'Authorized JavaScript origins' section and `http://localhost:8080/` this under the "Authorized redirect URIs"
7. Click save.
8. Once created, download the JSON file containing the client ID and secret and move it to the root of your project folder.
9. Rename the file to "client_secret.json"
10. Revisit the OAuth Consent Screen and under the test user section add your Gmail id.

NOTE: The Youtube Data API V3 is free to use, however it has pre-determined quota of 10,000 units/day. These 10,000 units are enough to transfer about 200 songs in one go (tested personally). Once the units over, any further request to the endpoint would return a 403 error. The quota is reset at midnight pacific time (12 A.M PT = 1.30 PM IST, same day).

## Run the app

Clone the project

```bash
  git clone https://github.com/dhruv-bvpdev/spotify-2-yt.git
```

Go to the project directory

```bash
  cd spotify-2-yt
```

Required Packages

```bash
  pip install google-auth google-auth-oauthlib google-auth-httplib2 spotipy pytube
```

Run the Script

```bash
python main.py <playlist_id>
```

NOTE: The playlist ID that needs to be used in the above command is the id of the same playlist you are trying to move to YT.

You can get this ID in the spotify playlist URL after `playlist/`

## Authors

- [@dhruv-bvpdev](https://www.github.com/dhruv-bvpdev)

## License

[MIT](https://github.com/dhruv-bvpdev/spotify-2-yt/blob/main/LICENSE)
