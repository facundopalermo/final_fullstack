"""fakesnews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from noticia.urls import router as noticia_router
from comentario.urls import router as comentario_router
from autor.urls import router as autor_router
from autor import views as autor

from django.contrib.auth.views import LogoutView

#router principal

router = routers.DefaultRouter()
router.registry.extend(noticia_router.registry)
router.registry.extend(comentario_router.registry)
router.registry.extend(autor_router.registry)


schema_view = get_schema_view(
    openapi.Info(
        title="Noticias Doradas",
        default_version="v1",
        description="Noticias para todos",
        contact=openapi.Contact(email="asd@gmail.com")
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', autor.LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', autor.ProfileView.as_view()),
    path('api/', include(router.urls)),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]