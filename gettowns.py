import requests
import json
def get_coordinates(town_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": town_name,
        "format": "json",
        "limit": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            # Extract latitude and longitude from the response
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            return float(lat), float(lon)
    return None

towns = [
 
    "Ammal",
    "Baghlia",
    "Ben Choud",
    "Beni Amrane",
    "Bordj Menaïel",
    "Boudouaou",
    "Boudouaou-El-Bahri",
    "Boumerdes",
    "Bouzegza Keddara",
    "Chabet el Ameur",
    "Corso",
    "Dellys",
    "Djinet",
    "El Kharrouba",
    "Hammedi",
    "Issers",
    "Khemis El-Khechna",
    "Larbatache",
    "Leghata",
    "Naciria",
    "Ouled Aïssa",
    "Ouled Hedadj",
    "Ouled Moussa",
    "Si Mustapha",
    "Sidi Daoud",
    "Souk El Had",
    "Taourga"
]

data_list = []
for town in towns:
    coordinates = get_coordinates(town)

    if coordinates:
        print(f"{town}: {coordinates}")
        data_list.append({"town": town, "coordinates": coordinates })

    else:
        print(f"No coordinates found for {town}")

# Write data to JSON file
with open("town_coordinates.json", "w") as json_file:
    json.dump(data_list, json_file, indent=4)

print("Data written to town_coordinates.json")