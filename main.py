import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Prompt user for date input
date = input("Which year do you want to travel to? Type date in YYYY-MM-DD format: ")

# Fetch Billboard Hot 100 chart for the specified date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
content = response.text
soup = BeautifulSoup(content, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Get Spotify credentials from environment variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Define the path for token.txt in the same directory as main.py
token_path = os.path.join(os.path.dirname(__file__), 'token.txt')

# Initialize Spotify API client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path=token_path,
    )
)

# Get the current user's Spotify ID
user_id = sp.current_user()["id"]
print(f"User ID: {user_id}")

# Initialize lists for song URIs and year
song_url = []
year = date.split("-")[0]

# Search for each song on Spotify and collect its URI
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_url.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new playlist on Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Created playlist: {playlist['external_urls']['spotify']}")

# Add collected songs to the new playlist
if song_url:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_url)
else:
    print("No songs were added to the playlist.")
