from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path("crear-organizacion", views.crear_organizacion, name="crear-organizacion"),
    path("crear-usuario", views.crear_usuario, name="crear-usuario"),
]