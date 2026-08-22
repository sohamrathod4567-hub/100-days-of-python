import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()
YOUR_APP_CLIENT_ID=os.getenv("CLIENT_ID")
YOUR_APP_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USERNAME = os.getenv("SPOTIFY_USERNAME")

date = input("What Year do you want to travel to ? (YYYY-MM-DD):")
URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"

response = requests.get(URL)
bill_bord_web_page = response.text
# print(bill_bord_web_page)

soup = BeautifulSoup(bill_bord_web_page, "html.parser")
song_titles=soup.find_all(name="h3",class_="chart-entry__title")
# print(song_titles)
song_list=[]

for song in song_titles:
    song_list.append(song.text)

print(song_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=YOUR_APP_CLIENT_ID,
        client_secret=YOUR_APP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]

song_uris=[]
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped")

# Create a new playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Billboard Hot 100 songs from {date}"
)

# Get playlist ID
playlist_id = playlist["id"]

# Add songs to playlist
sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris
)

print("Playlist created successfully!")