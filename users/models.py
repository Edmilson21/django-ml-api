from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ALUMNO = 'alumno'
    PROFESOR = 'profesor'
    ADMIN = 'admin'

    ROL_CHOICES = [
        (ALUMNO, 'Alumno'),
        (PROFESOR, 'Profesor'),
        (ADMIN, 'Administrador'),
    ]

    rol = models.CharField(
        max_length=10, 
        choices=ROL_CHOICES,
        default=ALUMNO
    )
    
    telefono = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.rol})"