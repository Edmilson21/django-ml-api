from django.urls import path
from .views import PrediccionView

urlpatterns = [
    path('predecir/', PrediccionView.as_view(), name='predecir'),
]