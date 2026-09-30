from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    creado_por = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'titulo', 'descripcion', 'creado_por', 'creado_en']