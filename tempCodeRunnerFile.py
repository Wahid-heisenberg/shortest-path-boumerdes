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

def get_bordering_towns(town_name):
    url = "http://overpass-api.de/api/interpreter"
    query = f"""
        [out:json];
        area[name="{town_name}"]->.searchArea;
        relation(area.searchArea)["boundary"="administrative"]->.boundary;
        relation.boundary["type"="administrative"]["admin_level"="8"];
        rel.boundary["name"]({{}})->.borderingTowns;
        foreach.borderingTowns -> .town(
          out;
          convert item::json;
          .town is_in->.townIsIn;
          .townIsIn out;
          convert rel::json;
          .townIsIn >->.town;
          .town >->.townIsIn;
          out;
        );
    """
    response = requests.post(url, data=query)
    if response.status_code == 200:
        data = response.json()
        towns = []
        for element in data["elements"]:
            if "tags" in element:
                town_name = element["tags"].get("name")
                if town_name:
                    towns.append(town_name)
        return towns
    return []

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
        bordering_towns = get_bordering_towns(town)
        print(f"{town}: {coordinates} : {bordering_towns} ")
        data_list.append({"town": town, "coordinates": coordinates, "bordering_towns": bordering_towns})
    else:
        print(f"No coordinates found for {town}")

# Write data to JSON file
with open("town_coordinates_with_borders.json", "w") as json_file:
    json.dump(data_list, json_file, indent=4)

print("Data written to town_coordinates_with_borders.json")
