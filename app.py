import spotipy, dotenv, os, time, json
from spotipy.oauth2 import SpotifyOAuth


dotenv.load_dotenv()

PLAYLIST_ID = os.getenv("PLAYLIST_ID")

scope = "user-library-read, playlist-modify-public, playlist-modify-private, playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

while True:
    # Get the user's saved tracks

    saved = sp.current_user_saved_tracks()
    playlist = sp.user_playlist("spotify", PLAYLIST_ID)

    # Check if the track is already in the playlist
    # If not, add it to the playlist
    for item in saved["items"]:
        track = item["track"]
        if track["id"] not in [t["track"]["id"] for t in playlist["tracks"]["items"]]:
            print(
                f"Adding {track['name']} by {track['artists'][0]['name']} to playlist"
            )
            sp.playlist_add_items(PLAYLIST_ID, [track["id"]])

    # Sleep for 1 min
    print("Loop finished, sleeping for 1 min")
    time.sleep(60)
