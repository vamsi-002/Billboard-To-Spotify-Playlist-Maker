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
- **python-dotenv**: For loading environment variables from a `.env` file.

## Installation

1. **Clone the repository:**
   git clone https://github.com/vamsi-002/Billboard-To-Spotify-Playlist-Maker.git

2. **Navigate to the project directory:**
    cd Billboard-To-Spotify-Playlist-Maker

3. **Install the required packages:**
    pip install requests beautifulsoup4 spotipy python-dotenv

## Setup Spotify API Credentials

To use the Spotify API, you need to set up your own Spotify Developer credentials. Follow these steps:

### Obtain Spotify API Credentials

1. **Create a Spotify Developer Account:**
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
   - Log in with your Spotify account or create a new one if you don’t have one.

2. **Create a New Application:**
   - Click "Create an App".
   - Fill out the application name and description. You can use something like "Billboard-To-Spotify-Playlist-Maker".
   - Accept the Spotify Developer Terms of Service.
   - Click "Create".

3. **Get Your Client ID and Client Secret:**
   - Once the application is created, you will be redirected to the app dashboard.
   - Here, you will find your Client ID and Client Secret.

4. **Set Up Redirect URI:**
   - Go to the "Edit Settings" of your application.
   - Add `http://example.com` as a Redirect URI. This is required for the OAuth process.

### Add Credentials to `.env` File

1. **Create a `.env` file** in your project directory (if it doesn't already exist).

2. **Add the following content** to your `.env` file:
   ```plaintext
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret

3. Replace "your_client_id" and "your_client_secret" with the credentials you obtained from the Spotify Developer Dashboard.