from django.db import models
from django.conf import settings
from django.utils import timezone

class Login(models.Model):
    user = models.EmailField(max_length=100)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.user


class Config(models.Model):
    OP_MODE = (
        ('0', 'Gateway'),
        ('1', 'Roteador'),
    )
    op_mode = models.CharField(max_length=1, choices=OP_MODE)

    def __str__(self):
        return self.op_mode
