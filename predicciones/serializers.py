from rest_framework import serializers

class PrediccionSerializer(serializers.Serializer):
    feature1 = serializers.FloatField()
    feature2 = serializers.FloatField() 