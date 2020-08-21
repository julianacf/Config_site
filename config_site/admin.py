from django.contrib import admin
from .models import Config_device
from .models import Status_device


# Register your models here.
admin.site.register(Config_device)
admin.site.register(Status_device)
