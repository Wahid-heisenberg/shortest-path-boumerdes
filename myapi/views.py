from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TownSerializer
import json
import os

from rest_framework import status
from .utils import find_shortest_path_with_visualization

json_file_path = os.path.join(os.path.dirname(__file__),  'town_coordinates.json')
print(json_file_path)

class TownListView(APIView):
    def get(self, request):
        # Load JSON data from the file
        with open(json_file_path, "r") as json_file:
            if json_file:
                json_data = json.load(json_file)
            else:
                json_data = []

        # Serialize the JSON data
        serializer = TownSerializer(json_data, many=True)
        
        # Return the serialized data as a response
        return Response(serializer.data)

class ShortestPathVisualization(APIView):
    def get(self, request, source_town, target_town):
        try:
            result = find_shortest_path_with_visualization(source_town, target_town)
            return Response({"result": result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)