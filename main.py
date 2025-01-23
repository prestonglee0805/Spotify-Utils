from Spotify_utils import *

def main():
    # Step 1: Welcome User
    welcome_user()

    # Step 2: Get Time Range
    time_range = get_time_range()

    # Step 3: Fetch Top Artists
    top_artists_data = fetch_top_artists(time_range)
    top_artists = top_artists_data["items"]

    # Step 4: Calculate Popularity Stats
    avg_popularity, popularity_scores = calculate_average_popularity(top_artists) 

    print(f"\nAverage popularity score of your top 50 artists in the past: {avg_popularity:.2f} \n")

    # Step 5: Display Top RANGE Artists 
    custom_range = choose_artist_range() 

    top_ten_artists = display_top_artists(top_artists, popularity_scores, custom_range)






#runs main code if _name_ is main
if __name__ == "__main__":
    main()