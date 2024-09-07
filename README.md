# Billboard-To-Spotify-Playlist-Maker

## Overview

**Billboard To Spotify Playlist Maker** is a Python application that transforms Billboard Hot 100 charts into Spotify playlists. This project integrates web scraping to extract song data from Billboard and utilizes the Spotify API to create and populate playlists on Spotify.

## Features

- Scrapes Billboard Hot 100 charts for a given date.
- Searches for the corresponding tracks on Spotify.
- Creates a private Spotify playlist with the top tracks from the Billboard chart.
- Manages authentication and token storage securely.

## Technologies Used

- **Python**: Programming language used for the application.
- **Requests**: For making HTTP requests to retrieve Billboard chart data.
- **BeautifulSoup**: For parsing and extracting data from HTML content.
- **Spotipy**: For interacting with the Spotify API.
