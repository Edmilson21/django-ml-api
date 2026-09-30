from rest_framework import serializers

class ImagenSerializer(serializers.Serializer):
    imagen = serializers.ImageField()