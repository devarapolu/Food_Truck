# Importing necessary modules
import os
import dotenv
import googlemaps
import logging as log
import pandas as pd
import time
import requests

log.basicConfig(level=log.INFO)

# Load environment variables from the .env file
dotenv.load_dotenv("APIKEY.env")

# Fetch the Google API key from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
YELP_API_KEY = os.getenv('YELP_API_KEY')
if not GOOGLE_API_KEY or not YELP_API_KEY:
    raise ValueError("Missing Google/YELP API Key in environment variables.")

# Initialize the client
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

# Close the underlying requests sessio    
gmaps.session.close()

def get_cuisine_from_yelp(restaurant_name, location="Indianapolis"):
    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}"
    }
    params = {
        "term": restaurant_name,
        "location": location
    }
    response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error with Yelp API. Status code: {response.status_code}")
        return None
    businesses = response.json().get("businesses")
    if not businesses:
        return None
    return ", ".join([category["title"] for category in businesses[0].get("categories", [])])

def extract_food_truck_info():
    try:
        search_results = gmaps.places(query="food trucks in Indianapolis")["results"]
        places = [
            {
                'Name': details['name'],
                'Address': details['formatted_address'],
                'Rating': details.get('rating'),
                'Website':gmaps.place(details['place_id'])["result"].get("website"),
                'Opening Hours': ", ".join(gmaps.place(details['place_id'])["result"].get("opening_hours", {}).get("weekday_text", [])),
                'Cuisine Type': get_cuisine_from_yelp(details['name']),
                'Latitude': details['geometry']['location']['lat'],
                'Longitude': details['geometry']['location']['lng']
            }
            for details in search_results
        ]
        pd.DataFrame(places, columns=['Name', 'Address', 'Rating', 'Website', 'Opening Hours', 'Cuisine Type','Latitude','Longitude']).to_csv("food_trucks.csv", index=False)
    except googlemaps.exceptions.ApiError as e:
        print(f"API error: {e}")
    except googlemaps.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except googlemaps.exceptions.Timeout as e:
        print(f"Request timed out: {e}")
    except googlemaps.exceptions.TransportError as e:
        print(f"Transport error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example Usage
if __name__ == "__main__":
    extract_food_truck_info()