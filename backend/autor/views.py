from rest_framework import viewsets, views, permissions, status, generics
from autor.models import AutorSerializer, AutorProfileSerializer
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from comentario.models import Comentario, ComentarioSerializer
from noticia.models import Noticia, NoticiaSerializer

from datetime import datetime

from django.contrib.auth import login

from autor.models import(
    Autor, 
    AutorSerializer,
    LoginSerializer
)

class AutorViewSet(viewsets.ModelViewSet):
    """Autor Resource"""
    queryset = Autor.objects.all().order_by("first_name")
    serializer_class = AutorSerializer

    @action(methods=['GET'], detail=True)
    def noticias(self, request, pk=None):

        autor = self.get_object()
        noticias = Noticia.objects.filter(autor=autor)

        context = {
            'request': request
        }

        fecha = self.request.GET.get('fecha')
        desde = self.request.GET.get('desde')
        hasta = self.request.GET.get('hasta')

        if fecha:
            fecha_date = datetime.strptime(fecha, "%d-%m-%Y").date()
            noticias = noticias.filter(fecha__date__range=[fecha_date, fecha_date])

        if desde:
            desde = datetime.strptime(desde, "%d-%m-%Y").date()
            noticias = noticias.filter(fecha__date__gte=desde)

        if hasta:
            hasta = datetime.strptime(hasta, "%d-%m-%Y").date()
            noticias = noticias.filter(fecha__date__lte=hasta) 

        noticia_serializer = NoticiaSerializer(noticias, many=True, context=context)
        return Response(noticia_serializer.data)
    
    @action(methods=['GET'], detail=True)
    def comentarios(self, request, pk=None):

        autor = self.get_object()
        comentario = Comentario.objects.filter(autor=autor)

        context = {
            'request': request
        }

        comentario_serializer = ComentarioSerializer(comentario, many=True, context=context)
        return Response(comentario_serializer.data)
        
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })

        serializer.is_valid(raise_exception=True)
        autor = serializer.validated_data['autor']
        login(request, autor)
        profile_serializer = AutorProfileSerializer(autor)
        return Response(profile_serializer.data, status=status.HTTP_202_ACCEPTED)


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AutorProfileSerializer
    
    def get_object(self):
        return self.request.user
