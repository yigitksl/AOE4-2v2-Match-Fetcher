#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import time

# Enter your Steam profile id
profile_id = '76561198328003169'

# API pagination settings
per_page = 50
page = 1
all_games = []
max_retries = 3

while True:
    url = f"https://aoe4world.com/api/v0/players/{profile_id}/games?game_type=rm_2v2&page={page}&per_page={per_page}"
    print(f"Fetching page {page} for player ID {profile_id}...")


while True:
    url = f"https://aoe4world.com/api/v0/players/76561198328003169/games?game_type=rm_2v2&page={page}&per_page={per_page}"
    print(f"Fetching page {page}...")
    
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()
            break  # Exit retry loop if request is successful
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            retries += 1
            time.sleep(5)  # Wait before retrying
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            retries += 1
            time.sleep(5)
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            retries += 1
            time.sleep(5)
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")
            retries += 1
            time.sleep(5)
        except json.JSONDecodeError as json_err:
            print(f"JSON Decode Error: {json_err}")
            retries += 1
            time.sleep(5)
    
    if retries == max_retries:
        print(f"Failed to fetch page {page} after {max_retries} retries.")
        break
    
    games = data.get('games', [])
    
    if not games:
        break
    
    all_games.extend(games)
    page += 1
    
    # Add a small delay to avoid hitting the API rate limit
    time.sleep(1)

print(f"Total games fetched: {len(all_games)}")

with open("all_games_2v2.json", "w") as f:
    json.dump(all_games, f, indent=4)



# In[ ]:




