from rest_framework import viewsets, permissions
# Create your views here.

from comentario.models import(
    Comentario,
    ComentarioSerializer
)

class ComentarioViewSet(viewsets.ModelViewSet):
    """Comentario Resource"""
    queryset=Comentario.objects.all().order_by("code")
    serializer_class = ComentarioSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)