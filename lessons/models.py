from django.db import models
from users.models import User

class Lesson(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
