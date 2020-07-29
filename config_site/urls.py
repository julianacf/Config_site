from django.urls import path
from . import views

urlpatterns = [
    path('', views.config, name='config'),
    path('', views.op_mode_select, name='op_mode_select')
]
