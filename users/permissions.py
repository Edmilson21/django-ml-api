from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'admin'

class IsProfesor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'profesor'

class IsAlumno(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'alumno'
    
    
    
#Permision para la vista en la app lesson, en sus views.py

class IsProfesorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol in ['profesor', 'admin']