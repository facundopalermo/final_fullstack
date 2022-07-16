from rest_framework import routers
from comentario.views import ComentarioViewSet

router = routers.DefaultRouter()
router.register(r"comentarios", ComentarioViewSet, "comentarios")