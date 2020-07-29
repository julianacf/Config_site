from django.contrib import admin
from .models import Login
from .models import Config
from .models import Connection

admin.site.register(Login)
admin.site.register(Config)
admin.site.register(Connection)

# Register your models here.
