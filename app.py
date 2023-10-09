import spotipy, dotenv, os, time
from spotipy.oauth2 import SpotifyOAuth

DELETE_AFTER_ADD = True

dotenv.load_dotenv()

PLAYLIST_ID = os.getenv("PLAYLIST_ID")

scope = "user-library-read, playlist-modify-public, playlist-modify-private, playlist-read-private, user-library-modify"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

while True:
    # Get the user's saved tracks

    saved = sp.current_user_saved_tracks()
    playlist = sp.user_playlist("spotify", PLAYLIST_ID)

    # Add any new tracks to the playlists
    for item in saved["items"]:
        track = item["track"]
        if track["id"] not in [t["track"]["id"] for t in playlist["tracks"]["items"]]:
            print(
                f"Adding {track['name']} by {track['artists'][0]['name']} to playlist"
            )
            sp.playlist_add_items(PLAYLIST_ID, [track["id"]])
            if DELETE_AFTER_ADD:
                print(f"Deleting {track['name']} from saved tracks")
                sp.current_user_saved_tracks_delete([track["id"]])
        else:
            print(
                f"{track['name']} by {track['artists'][0]['name']} already in playlist"
            )

    # Sleep for 1 min
    print("Loop finished, sleeping for 30 seconds")
    time.sleep(30)
