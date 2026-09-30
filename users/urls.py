from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView,ProfileView,AdminOnlyView,ProfesorOnlyView,AlumnoOnlyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'), # Esta vista no está en views.py, ya viene pré hecha en al instalar "pip install djangorestframework-simplejwt" 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Esta vista no está en views.py, ya viene pré hecha en al instalar "pip install djangorestframework-simplejwt" 
    path('profile/', ProfileView.as_view(), name='profile'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('profesor-only/', ProfesorOnlyView.as_view(), name='profesor-only'),
    path('alumno-only/', AlumnoOnlyView.as_view(), name='alumno-only'),
]
 