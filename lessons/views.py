from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Lesson
from .serializers import LessonSerializer
from users.permissions import IsProfesor, IsAdmin
from users.permissions import IsProfesorOrAdmin
from django.db.models import Q

""" Voy a comentar la clase LessonViewSet actual porque es menos eficiente en la búsqueda, el problema surgr que cuando tenemos muchas lesiones en la base de datos,
las búsquedas se vuelven lentas, tendremos el famoso problema de 'N+1 queries', debemos modificar 'Lesson.objects.all()' """

"""
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsProfesorOrAdmin()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)
"""

 # Con select_related solucionamos este problema
 
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.select_related('creado_por')
        
        # Búsqueda por título
        titulo = self.request.query_params.get('titulo')
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        
        # Filtrar por rol del creador
        rol = self.request.query_params.get('rol')
        if rol:
            queryset = queryset.filter(creado_por__rol=rol)
        
        busqueda = self.request.query_params.get('busqueda')
        if busqueda:
            queryset = queryset.filter(
                Q(titulo__icontains=busqueda) | Q(descripcion__icontains=busqueda)
            )
        
        return queryset
    
        

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsProfesorOrAdmin()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)
    