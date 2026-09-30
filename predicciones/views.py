from django.shortcuts import render
import joblib
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PrediccionSerializer
import os

# Cargamos el modelo UNA sola vez al arrancar Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
modelo = joblib.load(os.path.join(BASE_DIR, 'modelo.pkl'))

class PrediccionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PrediccionSerializer(data=request.data)
        if serializer.is_valid():
            datos = serializer.validated_data
            X = np.array([[datos['feature1'], datos['feature2']]])
            prediccion = modelo.predict(X)
            return Response({'prediccion': int(prediccion[0])})
        return Response(serializer.errors, status=400)
