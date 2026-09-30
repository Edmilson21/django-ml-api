from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView # clase de vistas personalizadas
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .models import User
from .permissions import IsAdmin, IsProfesor, IsAlumno


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
    

class ProfileView(APIView):
    '''
    permission_classes = [IsAuthenticated], Le dices a Django: 
    "solo deja entrar a usuarios que hayan hecho login y tengan un token válido.
     " Si no tienen token, devuelve 401 automáticamente — sin que tú escribas nada extra.
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        '''Aquí está la magia. Cuando el usuario manda el token en el header, D
        jango lo decodifica automáticamente y mete el objeto usuario en request.user.
        Es decir — request.user es el usuario que está haciendo la petición, ya listo para usar.'''
        
        user = request.user
        
        '''Devuelves un JSON con los datos del usuario. Response es la clase de DRF para devolver respuestas 
        — convierte automáticamente el diccionario Python en JSON.'''
        return Response({
            'username': user.username,
            'email': user.email,
            'rol': user.rol,
            'telefono': user.telefono
        })
        
  
       
# Conectanddo los permisos a las vistas

class AdminOnlyView(APIView):
    permission_classes = [IsAdmin] #permission_classes es una palabra reservada

    def get(self, request):
        return Response({
            'mensaje': 'Bienvenido Admin, tienes acceso total'
        })

class ProfesorOnlyView(APIView):
    permission_classes = [IsProfesor]

    def get(self, request):
        return Response({
            'mensaje': 'Bienvenido Profesor, puedes gestionar lecciones'
        }) 
        
        
class AlumnoOnlyView(APIView):
     permission_classes = [IsAlumno]
     
     def get(self, request):
         return Response({
                     'mensaje': 'Bienvenido Alumno'
                 }) 
         


