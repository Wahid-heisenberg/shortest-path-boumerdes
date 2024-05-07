from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TownSerializer
import json
import os
json_file_path = os.path.join(os.path.dirname(__file__),  'town_coordinates.json')
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
