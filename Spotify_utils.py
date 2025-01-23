import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# Spotify API setup
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8888/callback/"
SCOPE = "user-read-private user-top-read user-read-recently-played"

auth_manager = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
)
sp = spotipy.Spotify(auth_manager=auth_manager)

def welcome_user():
    #Welcome the user and display their Spotify display name.
    user = sp.current_user()
    print(f"Welcome {user['display_name']}!\n")
    return user 

def get_time_range():
    #Prompt the user to select a valid time range.

    valid_ranges = {"MONTH": "short_term", "6 MONTHS": "medium_term", "YEAR": "long_term"}
    print("Please select a time range (MONTH, 6 MONTHS, YEAR) for your Spotify data:")

    #remove leading or trailing spacese, converts all characters to uppercase
    time_range = input().strip().upper()

    #ensure that time_range is in valid_ranges 
    while time_range not in valid_ranges:
        print("Please select a VALID time range (MONTH, 6 MONTHS, YEAR):")
        time_range = input().strip().upper()


def fetch_top_artists(time_range):
    #Fetch the user's top 50 artists for the given time range
    return sp.current_user_top_artists(limit=50, time_range=time_range)

def calculate_average_popularity(artists): 

    #Concise way to create a new list. Get popularity key and its corresponding value from list of dictionaries. Each artist is its own separate dictionary containing name, popularity, etc.  

    #this creates a list of dictionaries {"name" : "...", "popularity" : ...}
    popularity_scores = {artist["name"]: artist["popularity"] for artist in artists} 
    #.values() to extract all values in dictionary 
    average_popularity = sum(popularity_scores.values()) / len(popularity_scores)
    return average_popularity, popularity_scores  

def choose_artist_range ():

    number = int(input("Select a number of artists to see popularity data on (1-50): ")) 

    while (number < 1 and number > 50):
        number = int(input("Select a VALID number of artists to see popularity data between 1 and 50: ")) 

    return number 

def display_top_artists(artists, popularity_scores, n): 

    names = [name["name"] for name in artists]
    #Display the top N artists with their popularity scores."""
    print(f"\nTOP {n} ARTISTS:\n") 

    for idx, name in enumerate(names, start=1): 
        #retrieve current popularity score with associated name 
        curr_pop_score = popularity_scores[name]
        print(f"{idx}. {name} with a popularity score of {curr_pop_score}\n") 

        if idx == n:
            break




