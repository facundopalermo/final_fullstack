from rest_framework import viewsets, permissions
from comentario.models import Comentario, ComentarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

from noticia.models import(
    Noticia,
    NoticiaSerializer
)

class NoticiaViewSet(viewsets.ModelViewSet):
    """Noticia Resource"""
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        noticias = Noticia.objects.all().order_by('-fecha')

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

        return noticias

    @action(methods=['GET'], detail=True)
    def comentarios(self, request, pk=None):

        noticia = self.get_object()
        comentario = Comentario.objects.filter(noticia=noticia)

        context = {
            'request': request
        }

        fecha = self.request.GET.get('fecha')
        desde = self.request.GET.get('desde')
        hasta = self.request.GET.get('hasta')

        if fecha:
            fecha_date = datetime.strptime(fecha, "%d-%m-%Y").date()
            comentario = comentario.filter(fecha__date__range=[fecha_date, fecha_date])

        if desde:
            desde = datetime.strptime(desde, "%d-%m-%Y").date()
            comentario = comentario.filter(fecha__date__gte=desde)

        if hasta:
            hasta = datetime.strptime(hasta, "%d-%m-%Y").date()
            comentario = comentario.filter(fecha__date__lte=hasta)

        comentario_serializer = ComentarioSerializer(comentario, many=True, context=context)
        return Response(comentario_serializer.data)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)