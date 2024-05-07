from math import radians, sin, cos, sqrt, atan2

def haversine(coord1, coord2):
    # Radius of the Earth in km
    R = 6371.0
    
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    return distance

def get_towns_with_shared_borders(town_name, towns_data, threshold_km=10):
    shared_border_towns = []

    # Find the coordinates of the given town
    town_coordinates = None
    for town in towns_data:
        if town["town"] == town_name:
            town_coordinates = town["coordinates"]
            break

    if town_coordinates:
        # Calculate distances to other towns
        for other_town in towns_data:
            if other_town["town"] != town_name:
                distance = haversine(town_coordinates, other_town["coordinates"])
                if distance <= threshold_km:
                    shared_border_towns.append(other_town["town"])

    return shared_border_towns

# Example usage
towns_data = [
    {
        "town": "Ammal",
        "coordinates": [
            36.6333486,
            3.5913032
        ]
    },
    {
        "town": "Baghlia",
        "coordinates": [
            36.795955199999995,
            3.867521059618945
        ]
    },
    {
        "town": "Ben Choud",
        "coordinates": [
            36.8641433,
            3.8801313
        ]
    },
    {
        "town": "Beni Amrane",
        "coordinates": [
            36.6678481,
            3.5918611
        ]
    },
    {
        "town": "Bordj Mena\u00efel",
        "coordinates": [
            36.7432364,
            3.7175665
        ]
    },
    {
        "town": "Boudouaou",
        "coordinates": [
            36.727203,
            3.408382
        ]
    },
    {
        "town": "Boudouaou-El-Bahri",
        "coordinates": [
            36.7721989,
            3.4044018
        ]
    },
    {
        "town": "Boumerdes",
        "coordinates": [
            36.7358032,
            3.6163045700585252
        ]
    },
    {
        "town": "Bouzegza Keddara",
        "coordinates": [
            36.6250914,
            3.4807733
        ]
    },
    {
        "town": "Chabet el Ameur",
        "coordinates": [
            36.634413300000006,
            3.67905992153962
        ]
    },
    {
        "town": "Corso",
        "coordinates": [
            36.7547423,
            3.4433833
        ]
    },
    {
        "town": "Dellys",
        "coordinates": [
            36.915798,
            3.913104
        ]
    },
    {
        "town": "Djinet",
        "coordinates": [
            36.8779905,
            3.720138
        ]
    },
    {
        "town": "El Kharrouba",
        "coordinates": [
            34.671565,
            9.427835141808348
        ]
    },
    {
        "town": "Hammedi",
        "coordinates": [
            36.6800253,
            3.2596049
        ]
    },
    {
        "town": "Issers",
        "coordinates": [
            36.693555700000005,
            3.691545946261125
        ]
    },
    {
        "town": "Khemis El-Khechna",
        "coordinates": [
            36.6505384,
            3.3317211
        ]
    },
    {
        "town": "Larbatache",
        "coordinates": [
            36.6379144,
            3.3710566
        ]
    },
    {
        "town": "Leghata",
        "coordinates": [
            36.78923975,
            3.6834189870120557
        ]
    },
    {
        "town": "Naciria",
        "coordinates": [
            36.7471933,
            3.836858
        ]
    },
    {
        "town": "Ouled A\u00efssa",
        "coordinates": [
            29.4235586,
            -0.0891357
        ]
    },
    {
        "town": "Ouled Hedadj",
        "coordinates": [
            36.7100229,
            3.3350379512863424
        ]
    },
    {
        "town": "Ouled Moussa",
        "coordinates": [
            36.6857409,
            3.3642924
        ]
    },
    {
        "town": "Si Mustapha",
        "coordinates": [
            36.7336375,
            3.6253478737864087
        ]
    },
    {
        "town": "Sidi Daoud",
        "coordinates": [
            36.8567267,
            3.8581586
        ]
    },
    {
        "town": "Souk El Had",
        "coordinates": [
            35.9567316,
            1.2462755
        ]
    },
    {
        "town": "Taourga",
        "coordinates": [
            36.7935601,
            3.9500124
        ]
    }
]

for town in towns_data:
    town_name = town["town"]
    shared_border_towns = get_towns_with_shared_borders(town_name, towns_data)
    print(f"Towns sharing borders with {town_name}: {shared_border_towns}")
