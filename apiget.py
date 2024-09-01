import requests
import pandas as pd

# Fetch data from OCEARCH or any other available shark tracking API
url = "https://www.mapotic.com/api/v1/maps/3413/pois.geojson/?h=20"  # Example endpoint
response = requests.get(url)
data = response.json()
# Ensure 'features' exists at the top level
shark_data = []
for feature in data['features']:
    # Extract coordinates
    coords = feature.get('geometry', {}).get('coordinates', [None, None])
    properties = feature.get('properties', {})

    # Append each shark's data to a list
    shark_data.append({
        'id': properties.get('id'),
        'name': properties.get('name'),
        'species': properties.get('species'),
        'length': properties.get('length'),
        'weight': properties.get('weight'),
        'tag_location': properties.get('tag_location'),
        'last_update': properties.get('last_update'),
        'stage_of_life': properties.get('stage_of_life'),
        'gender': properties.get('gender'),
        'latitude': coords[1],  # Extract latitude
        'longitude': coords[0],  # Extract longitude
        'last_ping': properties.get('zping_datetime')
    })

# Convert list to DataFrame
df = pd.DataFrame(shark_data)
