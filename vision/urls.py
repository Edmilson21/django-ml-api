from django.urls import path
from .views import DeteccionObjetosView

urlpatterns = [
    path('detectar/', DeteccionObjetosView.as_view(), name='detectar'),
]