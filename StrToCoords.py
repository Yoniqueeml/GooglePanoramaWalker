import requests


def get_coordinates(address):
    base_url = 'https://nominatim.openstreetmap.org/search?'

    params = {
        'q': address,
        'format': 'json',
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        return latitude, longitude
    else:
        print(f"I can't get coords for the: {address}")
        return None
