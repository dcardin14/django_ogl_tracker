from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_ogl/", views.add_ogl, name="add_ogl"),
    path('update_ogl/<int:pk>/', views.update_ogl, name='update_ogl'),
]