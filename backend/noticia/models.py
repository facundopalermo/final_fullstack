from datetime import datetime
from django.db import models
from autor.models import Autor, AutorSerializer
from rest_framework import serializers

# Create your models here.

class Noticia(models.Model):
    code = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(default=datetime.now())

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        null=False
    )

    def __str__(self) -> str:
        return f'{self.titulo}'

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

class NoticiaSerializer(serializers.ModelSerializer):

    #para cambiar el id de autor por el nombre
    autor = serializers.CharField(read_only=True)

    #traigo los datos del autor
    #autores = AutorSerializer(read_only=True)

    #recupero el id de autor
    autor_id = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all(), source="autor")

    class Meta: 
        model = Noticia
        fields = "__all__"
        #exclude = "titulo"