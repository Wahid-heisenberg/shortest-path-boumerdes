from rest_framework import serializers

class TownSerializer(serializers.Serializer):
    town = serializers.CharField()
    coordinates = serializers.ListField(child=serializers.FloatField())
