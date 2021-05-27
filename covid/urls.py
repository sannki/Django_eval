from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('send', views.send)
]