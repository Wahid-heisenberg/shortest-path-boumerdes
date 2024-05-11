import { useEffect, useRef, useState } from "react";
import mapboxgl from "mapbox-gl";

mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_KEY;

function App() {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const [sourceCity, setSourceCity] = useState("");
  const [destinationCity, setDestinationCity] = useState("");
  const cities = ["Paris", "Londres", "New York", "Tokyo", "Sydney"];

  useEffect(() => {
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: "mapbox://styles/mapbox/streets-v12",
      center: [-0.118092, 51.509865],
      zoom: 10,
    });

    return () => {
      if (map.current) {
        map.current.remove();
      }
    };
  }, []);

  const handleConfirmCities = async () => {
    try {
      if (!sourceCity || !destinationCity) {
        console.error("Veuillez sélectionner une ville source et une ville destination.");
        return;
      }
  
      const [sourceCoords, destinationCoords] = await Promise.all([
        getCoordinates(sourceCity),
        getCoordinates(destinationCity),
      ]);
  
      if (sourceCoords && destinationCoords) {
        // Afficher le chemin entre les villes sur la carte
        displayRoute(sourceCoords, destinationCoords);
      } else {
        console.error("Impossible de trouver les coordonnées de l'une des villes.");
      }
    } catch (error) {
      console.error("Erreur lors de la récupération des coordonnées :", error);
    }
  };
  
  const getCoordinates = async (city) => {
    try {
      const response = await fetch(
        `https://api.mapbox.com/geocoding/v5/mapbox.places/${city}.json?access_token=${mapboxgl.accessToken}`
      );
  
      if (!response.ok) {
        throw new Error("Impossible de récupérer les coordonnées.");
      }
  
      const data = await response.json();
      const coordinates = data.features[0].center;
      return { lng: coordinates[0], lat: coordinates[1] };
    } catch (error) {
      console.error("Erreur lors de la récupération des coordonnées :", error);
      return null;
    }
  };
  
  const displayRoute = (sourceCoords, destinationCoords) => {
    if (map.current) {
      const coordinates = [sourceCoords, destinationCoords];
      map.current.addSource("route", {
        type: "geojson",
        data: {
          type: "Feature",
          properties: {},
          geometry: {
            type: "LineString",
            coordinates: coordinates,
          },
        },
      });
  
      map.current.addLayer({
        id: "route",
        type: "line",
        source: "route",
        layout: {
          "line-join": "round",
          "line-cap": "round",
        },
        paint: {
          "line-color": "#888",
          "line-width": 8,
        },
      });
  
      map.current.fitBounds(coordinates, { padding: 100 });
    }
  };

  return (
    <>
     
      <div ref={mapContainer} id="map" className="map-container"></div>

      <div className="city-selector">
        <select
          value={sourceCity}
          onChange={(e) => setSourceCity(e.target.value)}
        >
          <option value="">Sélectionner une ville source</option>
          {cities.map((city, index) => (
            <option key={index} value={city}>
              {city}
            </option>
          ))}
        </select>

        <select
          value={destinationCity}
          onChange={(e) => setDestinationCity(e.target.value)}
        >
          <option value="">Sélectionner une ville destination</option>
          {cities.map((city, index) => (
            <option key={index} value={city}>
              {city}
            </option>
          ))}
        </select>

        <button onClick={handleConfirmCities}>Confirmer</button>
      </div>
    </>
  );
}

export default App;
