import requests
import pandas as pd
import os
import json
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox
import threading

# Function to fetch anime details from AniList API
def fetch_anime_data_anilist(page, per_page):
    query = '''
    query ($page: Int, $perPage: Int) {
      Page(page: $page, perPage: $perPage) {
        media(type: ANIME, sort: SCORE_DESC) {
          id
          title {
            romaji
            english
          }
          genres
          averageScore
        }
      }
    }
    '''
    variables = {
        'page': page,
        'perPage': per_page
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})

    if response.status_code == 200:
        data = response.json()
        return data['data']['Page']['media']
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
        print("Response Content:", response.text)
        return []

# Function to fetch additional details from MyAnimeList API
def fetch_anime_details_mal(anime_title):
    url = f"https://api.jikan.moe/v4/anime?q={anime_title}&limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            return data['data'][0]
    return None

# Fetch all genres from AniList API to display them to the user
def fetch_all_genres():
    query = '''
    query ($page: Int, $perPage: Int) {
      Page(page: $page, perPage: $perPage) {
        media(type: ANIME, sort: SCORE_DESC) {
          genres
        }
      }
    }
    '''
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': {'page': 1, 'perPage': 50}})
    
    if response.status_code == 200:
        data = response.json()
        anime_list = data['data']['Page']['media']
        all_genres = set()
        for anime in anime_list:
            all_genres.update(anime['genres'])
        return list(all_genres)
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
        print("Response Content:", response.text)
        return []

# Main function to fetch data and save to a file
def fetch_and_save_data(selected_genres, num_anime):
    anime_list = []
    page = 1
    per_page = 50  # Fetch 50 anime per page for efficiency

    while len(anime_list) < num_anime:
        new_anime = fetch_anime_data_anilist(page, per_page)
        if not new_anime:
            break  # Exit if no more data is fetched

        # Filter the new anime by the selected genres
        for anime in new_anime:
            if all(genre in anime['genres'] for genre in selected_genres):
                anime_list.append(anime)
                if len(anime_list) >= num_anime:
                    break
        page += 1

    filtered_anime = anime_list[:num_anime]

    detailed_anime_list = []
    for anime in filtered_anime:
        title = anime['title']['romaji']
        mal_details = fetch_anime_details_mal(title)
        if mal_details:
            anime_data = {
                'Title': title,
                'English Title': anime['title']['english'],
                'Genres': ', '.join(anime['genres']),
                'AniList Score': anime['averageScore'],
                'MAL Score': mal_details['score'],
                'MAL Members': mal_details['members'],
                'Synopsis': mal_details['synopsis']
            }
            detailed_anime_list.append(anime_data)

    # Ensure the directory exists
    output_dir = "D:\\Utkarsh\\code\\script\\chatgpt\\Anime Data"
    os.makedirs(output_dir, exist_ok=True)

    # Save to a new file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = os.path.join(output_dir, f"anime_data_{timestamp}.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(detailed_anime_list, f, ensure_ascii=False, indent=4)

    messagebox.showinfo("Success", f"Data saved to {output_file}")

# Main function to run the program
def main():
    all_genres = fetch_all_genres()
    if not all_genres:
        print("Could not fetch genres. Exiting.")
        return
    
    def on_submit():
        selected_genres = [genre.strip() for genre in genre_entry.get().split(',')]
        try:
            num_anime = int(num_anime_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Invalid number of anime. Exiting.")
            root.quit()
            return

        # Run the fetching and saving process in a separate thread
        threading.Thread(target=fetch_and_save_data, args=(selected_genres, num_anime)).start()

    # Create the GUI
    root = tk.Tk()
    root.title("Anime Data Fetcher")

    tk.Label(root, text="Enter the genres you want to filter by (comma-separated):").pack()
    genre_entry = tk.Entry(root, width=50)
    genre_entry.pack()

    tk.Label(root, text="Enter the number of anime to list:").pack()
    num_anime_entry = tk.Entry(root, width=10)
    num_anime_entry.pack()

    tk.Button(root, text="Submit", command=on_submit).pack()

    root.mainloop()

# Run the program
if __name__ == "__main__":
    main()
