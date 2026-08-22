# Day 46 - Spotify Playlist

## Overview

Day 46 of the 100 Days of Code - The Complete Python Pro Bootcamp.

In this project, I built a Spotify Playlist Generator using Python. The program takes a date from the user, scrapes the Billboard Hot 100 chart for that date, searches for the songs on Spotify, and creates a private Spotify playlist containing the available songs.

## Concepts Practiced

- Web scraping with Beautiful Soup
- Requests library
- Spotify API
- Spotipy
- OAuth authentication
- HTML parsing
- find_all()
- Lists
- Loops
- String manipulation
- Dictionaries
- API responses
- Exception handling
- Spotify track URIs
- Creating Spotify playlists
- Adding tracks to playlists

## How It Works

1. The user enters a date.
2. The program accesses the Billboard Hot 100 page for that date.
3. Beautiful Soup extracts the song titles.
4. Each song is searched on Spotify.
5. The Spotify track URI is collected.
6. A private Spotify playlist is created.
7. The songs are added to the playlist.

## How to Run

Install the required libraries:

    pip install requests beautifulsoup4 spotipy

Run the program:

    python main.py

Enter a date in this format:

    YYYY-MM-DD

Example:

    2020-08-22

The program will scrape the Billboard Hot 100 chart, search for the songs on Spotify, and create a private playlist.

## Example

    What Year do you want to travel to? (YYYY-MM-DD): 2020-08-22

    Playlist created successfully!

## What I Learned

This project taught me how to combine web scraping with an external API.

I learned how to extract information from a webpage using Beautiful Soup and then use that information to search Spotify. I also learned how OAuth authentication works and how Spotify track URIs can be used to create and populate playlists automatically.

## Project Status

Completed

Day 46 of 100 Days of Code.