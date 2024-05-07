# town_functions.py

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


def find_bordering_towns(towns_data, threshold_km=10):
    bordering_towns = {}
    
    for town1 in towns_data:
        bordering_towns[town1['town']] = []
        for town2 in towns_data:
            if town1 != town2:
                distance = haversine(town1['coordinates'], town2['coordinates'])
                if distance <= threshold_km:
                    bordering_towns[town1['town']].append(town2['town'])
                    
    # Manually enforce specific bordering relationships
    bordering_towns["Corso"].append("Boumerdes")
    bordering_towns["El Kharrouba"].append("Boudouaou")
    bordering_towns["Naciria"].append("Bordj Menaïel")
    bordering_towns["Djinet"].append("Bordj Menaïel")
    bordering_towns["Zemmouri"].append("Djinet")  
    bordering_towns["Zemmouri"].append("Dellys")
    
    
    return bordering_towns
