from rest_framework import routers
from noticia.views import NoticiaViewSet

router = routers.DefaultRouter()
router.register(r"noticias", NoticiaViewSet, "noticias")
