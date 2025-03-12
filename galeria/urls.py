from django.urls import path
from galeria.views import ViewGaleria

urlpatterns = [
    path('', ViewGaleria.as_view(),name='index'),
    path('/imagem/', ViewGaleria.as_view(),name='imagem'),
]