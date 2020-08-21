from django.urls import path
from . import views

urlpatterns = [
    path('', views.Config_device_View, name='config'),
    path('status/', views.Status_View, name='status'),
    #path('status/<int:id>', views.Status_device_View, name='status'),
]
