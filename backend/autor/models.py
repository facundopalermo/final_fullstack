from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from rest_framework import serializers
from noticia.models import models

from django.contrib.auth import authenticate

# Create your models here.

#class Autor(models.Model):
class Autor(AbstractUser):
    #nombre = models.CharField(max_length=250) -> first_name
    #apellido = models.CharField(max_length=250) -> last_name
    fecha_nac = models.DateField()
    #mail = models.EmailField(unique=True)
    email = models.EmailField(verbose_name='email', unique=True, max_length=255)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
class AutorSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()
    fecha_nac = serializers.DateField()

    def create (self, validate_data):
        instance = Autor()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.fecha_nac = validate_data.get('fecha_nac')
        instance.set_password(validate_data.get('password'))
        instance.save()
        instance.groups.add(Group.objects.get(name='Autor'))
        return instance

    def validate_username (self, data):
        users = Autor.objects.filter(username = data)
        if len(users)!=0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese otro.")
        else:
            return data
    
    def validate_email (self, data):
        users = Autor.objects.filter(email = data)
        if len(users)!=0:
            raise serializers.ValidationError("Este email ya está registrado, ingrese otro.")
        else:
            return data


    class Meta: 
        model = Autor
        #fields = "__all__"
        exclude = ["is_superuser", "is_staff", "is_active", "groups", "user_permissions", "last_login", "date_joined"]

class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(
        label="Email",
        write_only=True
    )

    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            autor = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not autor:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "email" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['autor'] = autor
        return attrs

class AutorProfileSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Autor
        #fields = "__all__"
        exclude = ["is_superuser", "is_staff", "is_active", "groups", "user_permissions", "password"]