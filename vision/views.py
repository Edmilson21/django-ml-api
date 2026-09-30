from django.shortcuts import render
import cv2
import numpy as np
from ultralytics import YOLO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ImagenSerializer

# Cargamos el modelo una sola vez
modelo_yolo = YOLO('yolov8n.pt')

class DeteccionObjetosView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ImagenSerializer(data=request.data)
        if serializer.is_valid():
            imagen = serializer.validated_data['imagen']
            
            # Convertir imagen a array numpy para OpenCV
            img_array = np.frombuffer(imagen.read(), np.uint8)
            img_cv = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            
            # Predicción con YOLOv8
            resultados = modelo_yolo(img_cv)
            
            # Extraer detecciones
            detecciones = []
            for r in resultados:
                for box in r.boxes:
                    detecciones.append({
                        'clase': modelo_yolo.names[int(box.cls)],
                        'confianza': round(float(box.conf), 2)
                    })
            
            return Response({'detecciones': detecciones})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
