from datetime import datetime
from django.db import models
from rest_framework import serializers
from noticia.models import Noticia
from autor.models import Autor

# Create your models here.

class Comentario(models.Model):
    code = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=250)
    fecha = models.DateTimeField(default=datetime.now())

    noticia = models.ForeignKey(
        Noticia,
        related_name='comentarios',
        on_delete=models.CASCADE,
        null=False
    )

    autor = models.ForeignKey(
        Autor,
        related_name='autor',
        on_delete=models.CASCADE,
        null=False
    )

    def __str__(self) -> str:
        return f'{self.autor} {"-"} {self.texto[:25]} {"..."}'

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

class ComentarioSerializer(serializers.ModelSerializer):

    autor = serializers.CharField(read_only=True)

    class Meta:
        model = Comentario
        fields= "__all__"