from django.urls import path
from . import views

urlpatterns = [
    path('', views.config, name='config'),
]
