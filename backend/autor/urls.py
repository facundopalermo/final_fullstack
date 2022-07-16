from rest_framework import routers
from autor.views import AutorViewSet

router = routers.DefaultRouter()
router.register(r"autores", AutorViewSet, "autores")